# Methods in this file are called by the map.py file. They are used to return a list of tuples. This list contains the markers we wanna draw on the map

import mysql.connector

# for env variables
from dotenv import load_dotenv
load_dotenv()
import os

mydb = mysql.connector.connect(
  host="localhost",
  user=os.getenv("user"),
  password=os.getenv("password"),
  database="credit_shelf",
  auth_plugin="mysql_native_password"
)

mycursor = mydb.cursor()

def get_coordinates_for_all_boroughs():
    crashMarkers = []

    sql = "SELECT latitude, longitude FROM crashes"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        if (x[0] and x[1]) is not None:
            lat = float(x[0])
            lon = float(x[1])
            crashMarkers.append((lat, lon,'<b>crash<b>', 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'))

    sql = "SELECT latitude, longitude FROM Stations"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        if (x[0] and x[1]) is not None:
            lat = float(x[0])
            lon = float(x[1])
            crashMarkers.append((lat, lon,'<b>station<b>', 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png'))

    return crashMarkers

def get_coordinates_for_borough(borough):
    if borough == "ALL":
        get_coordinates_for_all_boroughs()
    else:
        crashMarkers = []
        sql = "SELECT latitude, longitude FROM crashes WHERE borough = %s"
        borough = (borough,)

        mycursor.execute(sql, borough)

        myresult = mycursor.fetchall()

        for x in myresult:
            if (x[0] and x[1]) is not None:
                lat = float(x[0])
                lon = float(x[1])
                crashMarkers.append((lat, lon, '<b>crash<b>', 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'))

        sql = "SELECT latitude, longitude FROM Stations"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            if (x[0] and x[1]) is not None:
                lat = float(x[0])
                lon = float(x[1])
                crashMarkers.append((lat, lon,'<b>station<b>', 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png'))

        return crashMarkers
