import csv
import math
import random
import time

import requests

api_url = "https://geocode.search.hereapi.com/v1/geocode"
reve_url = "https://revgeocode.search.hereapi.com/v1/revgeocode"
# api_key = "oEZVAxUm0nfBQqOfxVSH91jOpP4B1HGtzpeeHREgXZo"
# api_key = "z3vHqCuRfGsIjUHDhHhA1BdavV26nsoW5UzwC5j1gBk"
# api_key ="g0zRSDgjtC_muIy1CStyI_hVIMrFCbU63QezqpHMCAU"
api_key = "ZAZmrZPYHYsaqMqkX1-ecbVHgEbNNR0LHrTRC1OAGGM"
# api_key = "NtDdX1_GSnZn_4cH85mz14FYdGb9wO1zo0gCUcdzG8k"

def extract_coordinates(item):
    position = item.get('position')
    return tuple(position.values()) if position else None


def generate_random_coordinates(center_lat, center_lon, radius_km, num_points):
    coordinates = []
    for _ in range(num_points):
        # Generate a random angle (in radians) and distance within the specified radius
        angle = random.uniform(0, 2 * math.pi)
        distance = random.uniform(0, radius_km)

        # Calculate the new latitude and longitude
        new_lat = center_lat + (180 / math.pi) * (distance / 6371) * math.cos(angle)
        new_lon = center_lon + (180 / math.pi) * (distance / 6371) * math.sin(angle)

        # Round latitude and longitude to 5 decimal places

        coordinates.append((new_lat, new_lon))
    return coordinates


def extend_zip_code(target_zip_code, api_key):
    global target_coord
    target_params = {
        'apikey': api_key,
        'q':  f"{target_zip_code}"
    }
    try:
        target_response = requests.get(api_url, params=target_params)
        print(target_response)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []
    target_data = target_response.json()
    if 'items' in target_data and target_data['items']:
        first_item = target_data['items'][0]
        address_info = first_item.get('address', {})
        postal_code = address_info.get('postalCode', '')

        if postal_code:
            target_coord = postal_code[:5]
        else:
            print("Postal code is not available for this address.")
    else:
        print("No items found in the 'items' array.")
    return target_coord

# Read ZIP codes from a CSV file and write results to a new CSV file
input_csv_filename = 'Zipcode.csv'
output_csv_filename = 'output_file.csv'

with open(input_csv_filename, 'r', newline='') as csvfile, open(output_csv_filename, 'w', newline='') as output_csvfile:
    reader = csv.DictReader(csvfile)
    fieldnames = reader.fieldnames + ['ZipCode']

    writer = csv.DictWriter(output_csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        target_zip = row['Address']+" "+row['City']
        print(target_zip)
        extended_zip_codes = extend_zip_code(target_zip, api_key)
        if extended_zip_codes:
            print(f"Extended postal codes for {target_zip}: {extended_zip_codes}")
            row['ZipCode'] = extended_zip_codes
            writer.writerow(row)
        else:
            print(f"Failed to extend postal codes for {target_zip}")
        time.sleep(1)

print(f"Results written to {output_csv_filename}")