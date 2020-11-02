import requests
import mysql.connector
import csv

# for env variables
from dotenv import load_dotenv
load_dotenv()
import os

mydb = mysql.connector.connect(
  host="localhost",
  user=os.getenv("user"),
  password=os.getenv("password"),
  auth_plugin="mysql_native_password",
  database="credit_shelf"
)

mycursor = mydb.cursor()

# This will store a list of tuples. Each tuple contains info about one station.
stations = []

with open('files/modified/combined/2019-citibike-tripdata-modified-combined.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            if row[0]:
                stationId = row[0]
            else:
                stationId = None
            stations.append((stationId, row[1], row[2], row[3]))
            line_count += 1
    print(f'Processed {line_count} lines.')

sql = "INSERT INTO Stations (stationId, name, latitude, longitude) VALUES (%s, %s, %s, %s)"
val = (stations)
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "rows inserted.")
