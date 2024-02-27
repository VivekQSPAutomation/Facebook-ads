import csv
import io
from math import radians

import numpy as np
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.requests import Request
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pandas import pandas as pd

app = FastAPI()

templates = Jinja2Templates(directory="templates")

df = pd.read_csv('zip_updated.csv')
df.dropna(subset=['lat', 'lon'], inplace=True)


def format_postcode(code):
    return f'{int(code):05d}'


def filter_postcodes(lat, long, distance_threshold):
    lat, long = radians(lat), radians(long)
    lat2, lon2 = np.radians(df['lat'].values), np.radians(df['lon'].values)
    dlon = lon2 - long
    dlat = lat2 - lat
    a = np.sin(dlat / 2) ** 2 + np.cos(lat) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    dist = 3959 * c
    postcodes = df.loc[dist <= distance_threshold, 'code'].apply(format_postcode).tolist()
    return postcodes


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/upload")
async def upload_csv(request: Request, file: UploadFile = File(...), radius: int = Form(...)):
    radius_km = radius
    second_data_df = pd.read_csv(io.BytesIO(await file.read()))
    df = pd.read_csv('zip_updated.csv')
    zip_column_1 = df['code']
    zip_column_2 = second_data_df['code']
    common_zips = set(zip_column_1) & set(zip_column_2)
    common_zips_data = df[df['code'].isin(common_zips)]
    common_zips_lat_long = common_zips_data[['lat', 'lon', 'code']]
    json_string = common_zips_lat_long.values.tolist()

    # filename, ext = os.path.splitext(file.filename)
    # cleaned_filename = ''.join(c if c.isalnum() or c in ['.', '_'] else '_' for c in filename)
    csv_file = f"output.csv"
    with open(csv_file, 'w', newline='') as csvfile:
        fieldnames = ['ZipCode', 'Extended Zipcodes']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for lat, long, code in json_string:

            extended_zip_codes = filter_postcodes(lat, long, radius_km)
            extend = ",".join(extended_zip_codes)
            writer.writerow({'ZipCode': format_postcode(int(code)), 'Extended Zipcodes': extend})

    download_url = f"/download/{csv_file}"
    return templates.TemplateResponse("index.html", {"request": request, "file_name": csv_file,
                                                     "message": "File process successfully", "success": True,
                                                     "download_url": download_url})


@app.get("/download/{filename}")
def download_file(filename: str):
    file_path = f"./{filename}"
    return FileResponse(file_path, filename=filename, media_type='text/csv')
