# A small CLI that returns info about injured or killed cyclists by borough
## Stage 0

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
borough = input("Please enter a borough of NY:\n")
borough = borough.upper()

# defining a params dict for the parameters to be sent to the API
PARAMS = {'borough':borough}

# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)

# extracting data in json format
data = r.json()

# print(data)

for i in data:
    injuredCyclist = i.get("number_of_cyclist_injured")
    killedCyclist = i.get("number_of_cyclist_killed")
    if (int(injuredCyclist) > 0 or int(killedCyclist) > 0):
        print(i)
