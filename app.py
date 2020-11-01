from flask import Flask, jsonify, request, render_template
from flask_googlemaps import GoogleMaps

app = Flask(__name__, template_folder='website')

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyAwOC5SGtMDCwI854eq7dQwcqMKSxOZb_Y"

# Initialize the extension
GoogleMaps(app)

@app.route('/')
def landing_page():
    return render_template('index.html')
