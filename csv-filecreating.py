# a automation for creating google calendar schedule
# it should be creating a csv file

import csv  
import os
from datetime import datetime

import json


# #data
# Subject,Start Date,Start Time,End Date,End Time,All Day Event,Description,Location,Private


data_file = 'data.json'
with open(data_file, 'r') as file:
    data = json.load(file)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"Schedule '{timestamp}'.csv"

if not os.path.exists(filename):
    with open(filename, mode="w", newline="") as file:
        fieldnames = ["Subject", "Start Date", "Start Time", "End Date", "End Time", "All Day Event", "Description", "Location", "Private"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for row in data: 
            writer.writerow(row)

    print(f"CSV File '{filename}' created sucessfull")
else: 
    print(f"CSV File '{filename}' error")