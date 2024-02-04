

from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import FileResponse
import shutil
import os
import csv
import math
import random
import time
import requests
from starlette.websockets import WebSocket
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


templates = Jinja2Templates(directory="templates")

api_url = "https://geocode.search.hereapi.com/v1/geocode"
reve_url = "https://revgeocode.search.hereapi.com/v1/revgeocode"
api_key = "NtDdX1_GSnZn_4cH85mz14FYdGb9wO1zo0gCUcdzG8k"


def extract_coordinates(item):
    position = item.get('position')
    return tuple(position.values()) if position else None


def generate_random_coordinates(center_lat, center_lon, radius_km, num_points):
    coordinates = []
    for _ in range(num_points):
        angle = random.uniform(0, 2 * math.pi)
        distance = random.uniform(0, radius_km)
        new_lat = center_lat + (180 / math.pi) * (distance / 6371) * math.cos(angle)
        new_lon = center_lon + (180 / math.pi) * (distance / 6371) * math.sin(angle)
        coordinates.append((new_lat, new_lon))
    return coordinates


def extend_zip_code(target_zip_code, api_key, extend_distance, num_points):
    global target_coord
    target_params = {'apikey': api_key, 'qq': f"postalCode={target_zip_code}"}
    try:
        target_response = requests.get(api_url, params=target_params)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []
    target_data = target_response.json()
    if target_data['items']:
        target_coord = extract_coordinates(target_data['items'][0])
    else:
        return []
    if not target_coord:
        return []
    lat, lon = target_coord
    nearby_coordinates = generate_random_coordinates(lat, lon, extend_distance, num_points)
    extended_zip_codes = []
    for coord in nearby_coordinates:
        extended_params = {'apikey': api_key, 'at': f"{coord[0]},{coord[1]}", 'lang': "en-US"}
        try:
            extended_response = requests.get(reve_url, params=extended_params)
            extended_data = extended_response.json()
            if extended_data['items']:
                postal_code = extended_data['items'][0]['address'].get('postalCode', '')
                if postal_code:
                    extended_zip_codes.append(postal_code)
                else:
                    print(f"Postal code not found for coordinates {coord}")
            else:
                print('No item to add')
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            continue
    return extended_zip_codes


def process_csv(input_filename, output_filename, radius):
    with open(input_filename, 'r', newline='') as csvfile, open(output_filename, 'w', newline='') as output_csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames + ['ExtendedPostalCodes']
        writer = csv.DictWriter(output_csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            target_zip = row['Zipcode']
            num_points = 5
            miles = radius * 1.60934
            extended_zip_codes = extend_zip_code(target_zip, api_key, extend_distance=miles,
                                                 num_points=num_points)

            if extended_zip_codes:
                print(f"Extended postal codes for {target_zip}: {extended_zip_codes}")
                row['ExtendedPostalCodes'] = extended_zip_codes
                writer.writerow(row)
            else:
                print(f"Failed to extend postal codes for {target_zip}")
            time.sleep(1)

    print(f"Results written to {output_filename}")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



@app.post("/upload/")
async def create_upload_file(request: Request,file: UploadFile = File(...), radius: int = Form(...)):
    # Process the file and radius
    input_filename = 'temp_input_file.csv'
    output_filename = f'{os.path.splitext(file.filename)[0]}_extend.csv'

    with open(input_filename, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    total_rows = sum(1 for line in open(input_filename))
    with open(output_filename, 'w', newline='') as output_csvfile:
        reader = csv.DictReader(open(input_filename, 'r', newline=''))
        fieldnames = reader.fieldnames + ['ExtendedPostalCodes']
        writer = csv.DictWriter(output_csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i, row in enumerate(reader):
            target_zip = row['Zipcode']

            num_points = 5
            extended_zip_codes = extend_zip_code(target_zip, api_key, extend_distance=radius, num_points=num_points)

            if extended_zip_codes:
                row['ExtendedPostalCodes'] = extended_zip_codes
                writer.writerow(row)

            time.sleep(1)

    os.remove(input_filename)
    download_url = f"/download/{output_filename}"
    return templates.TemplateResponse("index.html", {"request": request,"file_name":output_filename ,"message":"File process successfuully", "success": True, "download_url": download_url})


@app.get("/download/{filename}")
def download_file(filename: str):
    file_path = f"./{filename}"  # Make sure the file path is correct
    return FileResponse(file_path, filename=filename, media_type='text/csv')

