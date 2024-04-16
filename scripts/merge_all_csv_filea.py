# INSERT ALL REAL DATA INTO ONE CSV FILE: real_windspeed.csv
# =================================================
import os
import json
import csv

print("\n\nINSERT ALL REAL DATA INTO ONE CSV FILE: real_windspeed.csv\n")

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Create CSV folder
csv_real_data_folder = "real-data"
create_folder_if_not_exists(csv_real_data_folder)

# Write forecast data (from API) to CSV file
merged_csv_real_data_file_path = "real-data/real_windspeed.csv"

# Write headers to the CSV file
with open(merged_csv_real_data_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    headers = ["PCTimeStamp", "HD01_Ambient WindSpeed Avg. (1)", "HD02_Ambient WindSpeed Avg. (2)", 
               "HD03_Ambient WindSpeed Avg. (3)", "HD04_Ambient WindSpeed Avg. (4)", "HD05_Ambient WindSpeed Avg. (5)", 
               "HD06_Ambient WindSpeed Avg. (6)","HD07_Ambient WindSpeed Avg. (7)", "HD08_Ambient WindSpeed Avg. (8)"]
    writer.writerow(headers)

# Specify the folder path containing all .csv files of real data of windspeed
wind_farm_folder_path = "Preprocessed-HD-Farm"

# Get a list of all files in the folder
element_csv_real_data_files = sorted(os.listdir(wind_farm_folder_path))

with open(merged_csv_real_data_file_path, 'a', newline='') as merged_file:
    merged_writer = csv.writer(merged_file)

    # Iterate over each file to process
    for csv_file_name in element_csv_real_data_files:
        element_csv_file_path = os.path.join(wind_farm_folder_path, csv_file_name)
        print("element_csv_file_path = ", element_csv_file_path)

        # Open each CSV file in read mode
        with open(element_csv_file_path, 'r') as element_file:
            element_reader = csv.reader(element_file)
            header_skipped = False
            for row in element_reader:
                if not header_skipped:
                    header_skipped = True
                    continue  # Skip the header row
                # Write the data row to the output CSV file
                merged_writer.writerow(row)