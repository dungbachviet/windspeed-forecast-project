import json
from datetime import datetime

# Load data from JSON file
with open('forecast_data.json', 'r') as file:
    data = json.load(file)

# Access each field
timestamp_list = data['ts']
units = data['units']
wind_u_150h = data['wind_u-150h']
wind_v_150h = data['wind_v-150h']
warning = data['warning']

# # Print or use the data as needed
# print("Timestamps:", timestamp_list)
# print("Units:", units)
# print("Wind u-150h:", wind_u_150h)
# print("Wind v-150h:", wind_v_150h)
# print("Warning:", warning)

print("Wind u-150h:", len(wind_u_150h))
print("Wind v-150h:", len(wind_v_150h))

for timestamp, wind_u, wind_v in zip(timestamp_list, wind_u_150h, wind_v_150h):
    second_timestamp = timestamp / 1000
    datetime_timestamp = datetime.fromtimestamp(second_timestamp)
    print("\n datetime_timestamp = ", datetime_timestamp)
    print("timestamp: ", timestamp, "wind_u: ", wind_u, "wind_v: ", wind_v)
    