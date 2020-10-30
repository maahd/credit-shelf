# Stage 1

# importing the requests library
import requests
import mysql.connector

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

# api-endpoint
URL = "https://data.cityofnewyork.us/resource/h9gi-nx95.json"

# Uncomment to ask the user for input
borough = input("Please enter a borough of NY. Information for killed or injured cyclists will be added to your database:\n")
borough = borough.upper()

# Comment to ask the user for input
# borough = "QUEENS"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'borough':borough}

# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)

# extracting data in json format
data = r.json()

crashes = []

for i in data:

    crossStreetName = i.get("cross_street_name")
    if crossStreetName:
        crossStreetName = ' '.join(crossStreetName.split())
    else:
        crossStreetName = None

    injuredCyclist = i.get("number_of_cyclist_injured")
    killedCyclist = i.get("number_of_cyclist_killed")

    if (int(injuredCyclist) > 0 or int(killedCyclist) > 0):
        crashes.append((
                        i["crash_date"],
                        i["crash_time"],
                        i["borough"],
                        i.get("zip_code", None),
                        i.get("latitude", None),
                        i.get("longitude", None),
                        crossStreetName,
                        i["number_of_persons_injured"],
                        i["number_of_persons_killed"],
                        i["number_of_pedestrians_injured"],
                        i["number_of_pedestrians_killed"],
                        i["number_of_cyclist_injured"],
                        i["number_of_cyclist_killed"],
                        i["number_of_motorist_injured"],
                        i["number_of_motorist_killed"],
                        i.get("contributing_factor_vehicle_1", None),
                        i.get("contributing_factor_vehicle_2", None),
                        i["collision_id"],
                        i.get("vehicle_type_code1", None),
                        i.get("vehicle_type_code2", None)
                      ))

sql = "INSERT INTO Crashes (crashDate, crashTime, borough, zipCode, latitude, longitude, crossStreetName, numberOfPersonsInjured, numberOfPersonsKilled, numberOfPedestriansInjured, numberOfPedestriansKilled, numberOfCyclistInjured, numberOfCyclistKilled, numberOfMotoristInjured, numberOfMotoristKilled, contributingFactorVehicle1, contributingFactorVehicle2, collisionId, vehicleTypeCode1, vehicleTypeCode2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = (crashes)
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "rows inserted.")
