import random
import math

import requests


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

    extended_zip_codes = []
    for coord in coordinates:
        extended_params = {
            'apikey': "z3vHqCuRfGsIjUHDhHhA1BdavV26nsoW5UzwC5j1gBk",
            'at': f"{coord[0]},{coord[1]}",
            'lang': "en-US"
        }
        print(coord[0], coord[1])
        try:
            extended_response = requests.get("https://revgeocode.search.hereapi.com/v1/revgeocode",
                                             params=extended_params)
            extended_data = extended_response.json()
            print(extended_data)
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


# Example usage:
center_latitude = 40.7128  # Example latitude (e.g., New York City)
center_longitude = -74.0060  # Example longitude (e.g., New York City)
radius_in_km = 2  # Example radius in kilometers
num_points_to_generate = 50  # Example number of points to generate

random_coordinates = generate_random_coordinates(center_latitude, center_longitude, radius_in_km,
                                                 num_points_to_generate)

print(random_coordinates)
