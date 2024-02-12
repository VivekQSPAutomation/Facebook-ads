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
import httpx
import asyncio
import requests
from starlette.websockets import WebSocket
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

templates = Jinja2Templates(directory="templates")

api_url = "https://geocode.search.hereapi.com/v1/geocode"
reve_url = "https://revgeocode.search.hereapi.com/v1/revgeocode"
api_key = "oEZVAxUm0nfBQqOfxVSH91jOpP4B1HGtzpeeHREgXZo"

def extract_coordinates(item):
    position = item.get('position')
    return tuple(position.values()) if position else None


def generate_random_coordinates(center_lat, center_lon, radius_km, num_points):
    csv_file ="Coordinates.csv"
    coordinates = []
    with open(csv_file,'a', newline='') as csvfile:
        fieldnames = ['Latitude', 'Longitude']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(num_points):
            angle = random.uniform(0, 2 * math.pi)
            new_lat = center_lat + (180 / math.pi) * (radius_km / 6371) * math.cos(angle)
            new_lon = center_lon + (180 / math.pi) * (radius_km / 6371) * math.sin(angle)
            coordinates.append((new_lat, new_lon))
            writer.writerow({'Latitude': new_lat, 'Longitude': new_lon})
    return coordinates

async def make_api_request(url, params):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, params=params)
            return response.json()
        except httpx.HTTPError as e:
            print("response error")
            return None
        except httpx.RequestError as e:
            print(f"Request error: {e}")
            return None

async def extend_zip_code_async(target_zip_code, api_key, extend_distance,num_points):
    target_params = {'apikey': api_key, 'qq': f"postalCode={target_zip_code};country=United States"}
    target_data = await make_api_request(api_url, target_params)
    if target_data and target_data.get('items'):
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
        extended_data = await make_api_request(reve_url, extended_params)
        if extended_data and extended_data.get('items'):
            postal_code = extended_data['items'][0]['address'].get('postalCode', '')
            if postal_code:
                extended_zip_codes.append(postal_code)
            else:
                print(f"Postal code not found for coordinates {coord}")
        else:
            print('No item to add')

    return extended_zip_codes




@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



@app.post("/upload/")
async def create_upload_file(request: Request,file: UploadFile = File(...), radius: int = Form(...)):
    # Process the file and radius
    input_filename = 'temp_input_file.csv'
    output_filename = f'output_extend.csv'
    lat_file ="lat_long.csv"

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
            radius_km = radius * 1.60934
            num_points = 100
            extended_zip_codes = await extend_zip_code_async(target_zip, api_key, extend_distance=radius_km, num_points=num_points)

            if extended_zip_codes:
                row['ExtendedPostalCodes'] = extended_zip_codes
                writer.writerow(row)

            time.sleep(1)

    os.remove(input_filename)
    download_url = f"/download/{output_filename}"
    return templates.TemplateResponse("index.html", {"request": request,"file_name":output_filename ,"message":"File process successfuully", "success": True, "download_url": download_url})


@app.get("/download/{filename}")
def download_file(filename: str):
    file_path = f"./{filename}"
    return FileResponse(file_path, filename=filename, media_type='text/csv')

