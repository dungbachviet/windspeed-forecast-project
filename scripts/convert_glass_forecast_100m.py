# CONVERT GLASS-FORECAST 100M WINDSPEED TO CSV FILE: glass_forecast_100m.csv
# =================================================

import os
import json
import csv

print("\n\nCONVERT GLASS-FORECAST 100M WINDSPEED TO CSV FILE: glass_forecast_100m.csv\n")

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Create CSV folder
csv_folder_path = "csv"
create_folder_if_not_exists(csv_folder_path)


# Specify the folder path containing all .json files of forecasting windspeed for 100m
folder_path = 'glass-forecast/100m'

# Write forecast data (from API) to CSV file
csv_file_path = "csv/glass_forecast_100m.csv"

# Write headers to the CSV file
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    headers = ['time', 'noaa', 'sg']
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
        for index, time_windspeed in enumerate(forecast_data["hours"]):
            if index < 24:
                writer.writerow([time_windspeed["time"], time_windspeed["windSpeed100m"]["noaa"], time_windspeed["windSpeed100m"]["sg"]])
