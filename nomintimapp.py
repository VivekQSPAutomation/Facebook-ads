import csv
import io
import math
import random

import requests
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.requests import Request
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pandas import pandas as pd

app = FastAPI()

templates = Jinja2Templates(directory="templates")


def reverse_geocode(latitude, longitude):
    url = f"https://nominatim.openstreetmap.org/reverse?lat={latitude}&lon={longitude}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        address = data.get('address', '')
        if address:

            postcode = address.get('postcode', '')
            if postcode:
                return postcode
            else:
                pass
        else:
            pass
    else:
        print("Error:", response.status_code)
        return None


def generate_random_coordinates(center_lat, center_lon, radius_km, num_points):
    csv_file = "Coordinates.csv"
    coordinates = []
    with open(csv_file, 'a', newline='') as csvfile:
        fieldnames = ['Latitude', 'Longitude']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(num_points):
            angle = random.uniform(0, 2 * math.pi)
            new_lat = center_lat + (180 / math.pi) * (radius_km / 6371) * math.cos(angle)
            new_long = center_lon + (180 / math.pi) * (radius_km / 6371) * math.sin(angle)
            new_la = round(new_lat, 6)
            new_lon = round(new_long, 6)
            coordinates.append([new_la, new_lon])
            writer.writerow({'Latitude': new_la, 'Longitude': new_lon})
    return coordinates


def extend_zip_code_async(lat, long, extend_distance, num_points):
    matched_zip_list = []
    lat_long_values = generate_random_coordinates(lat, long, extend_distance, num_points)
    for lat, lon in lat_long_values:
        check = reverse_geocode(lat, long)
        if check:
            matched_zip_list.append(check)
        else:
            pass
    return matched_zip_list


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/upload")
async def upload_csv(request: Request, file: UploadFile = File(...), radius: int = Form(...)):
    radius_km = radius * 1.60934
    second_data_df = pd.read_csv(io.BytesIO(await file.read()))
    df = pd.read_csv('zip_updated.csv')
    zip_column_1 = df['code']
    zip_column_2 = second_data_df['code']
    common_zips = set(zip_column_1) & set(zip_column_2)
    common_zips_data = df[df['code'].isin(common_zips)]
    common_zips_lat_long = common_zips_data[['lat', 'lon', 'code']]
    json_string = common_zips_lat_long.values.tolist()
    csv_file = "output.csv"
    with open(csv_file, 'w', newline='') as csvfile:
        fieldnames = ['ZipCode', 'Extended Zipcodes']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for lat, long, code  in json_string:
            unique_zip_codes = set()
            extended_zip_codes = extend_zip_code_async(lat, long, radius_km, num_points=100)
            unique_zip_codes.update(extended_zip_codes)
            writer.writerow({'ZipCode': code, 'Extended Zipcodes': list(unique_zip_codes)})

    download_url = f"/download/{csv_file}"
    return templates.TemplateResponse("index.html", {"request": request, "file_name": csv_file,
                                                     "message": "File process successfully", "success": True,
                                                     "download_url": download_url})


@app.get("/download/{filename}")
def download_file(filename: str):
    file_path = f"./{filename}"
    return FileResponse(file_path, filename=filename, media_type='text/csv')
