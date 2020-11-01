from flask import Flask, jsonify, request, render_template
from flask_googlemaps import GoogleMaps

# for env variables
from dotenv import load_dotenv
load_dotenv()
import os

app = Flask(__name__, template_folder='website')

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = os.getenv("googleMapsApiKey")

# Initialize the extension
GoogleMaps(app)

@app.route('/')
def landing_page():
    return render_template('index.html')
