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


def get_coordinates_for_borough(borough):
    crashMarkers = []
    sql = "SELECT latitude, longitude FROM crashes WHERE borough = %s"
    borough = (borough,)

    mycursor.execute(sql, borough)

    myresult = mycursor.fetchall()

    for x in myresult:
        if (x[0] and x[1]) is not None:
            lat = float(x[0])
            lon = float(x[1])
            crashMarkers.append((lat, lon))

    return crashMarkers
