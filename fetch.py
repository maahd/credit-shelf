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
    sql = "SELECT latitude, longitude FROM crashes WHERE borough = %s"
    borough = (borough,)

    mycursor.execute(sql, borough)

    myresult = mycursor.fetchall()

    for x in myresult:
      print(x)

get_coordinates_for_borough("QUEENS")
