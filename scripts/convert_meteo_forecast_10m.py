# CONVERT METEO-FORECAST 100M WINDSPEED TO CSV FILE: meteo_forecast_10m.csv
# =================================================

import os
import json
import csv

print("\n\nCONVERT METEO-FORECAST 100M WINDSPEED TO CSV FILE: meteo_forecast_10m.csv\n")

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Create CSV folder
csv_folder_path = "csv"
create_folder_if_not_exists(csv_folder_path)

# Specify the folder path containing all .json files of forecasting windspeed for 10m
folder_path = 'meteo-forcast/10m'

# Write forecast data (from API) to CSV file
csv_file_path = "csv/meteo_forcast_10m.csv"

# Write headers to the CSV file
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    headers = ['time', 'meteo']
    writer.writerow(headers)

# Get a list of all files in the folder
json_files = sorted(os.listdir(folder_path))

# Iterate over each file to process
for file_name in json_files:
    # Construct the full file path
    file_path = os.path.join(folder_path, file_name)
    print("file_path = ", file_path)

    # Open and load the JSON file containing forecast data
    with open(file_path, 'r') as file:
        forecast_data = json.load(file)

    # Open CSV file to write forecast data of this current file
    with open(csv_file_path, 'a', newline='') as file:
        writer = csv.writer(file)

        # Write newest 24 forecast datapoints of this file to the CSV file
        for index, time_windspeed in enumerate(zip(forecast_data["hourly"]["time"], forecast_data["hourly"]["wind_speed_10m"])):
            print(time_windspeed)
            if index < 24:
                writer.writerow([time_windspeed[0]+":00+00:00", time_windspeed[1]])
