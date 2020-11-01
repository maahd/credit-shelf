from flask import Flask, render_template, request
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

from fetch import get_coordinates_for_borough, get_coordinates_for_all_boroughs

app = Flask(__name__, template_folder=".")
GoogleMaps(app)

boroughs = ["ALL", "MANHATTAN", "QUEENS", "BROOKLYN", "BRONX"]

@app.route("/")
def mapview():
    crashMarkers = get_coordinates_for_all_boroughs()
    # creating a map in the view
    sndmap = Map(
        identifier="sndmap",
        lat=40.7128,
        lng=-74.0060,
        markers=crashMarkers,
        zoom=11
        #fit_markers_to_bounds = True
    )
    return render_template('./website/map.html', sndmap=sndmap, boroughs=boroughs, selectedBorough=boroughs[0])

@app.route("/selectBorough", methods=['POST'])
def selectBorough():
    selectedBorough = request.form.get('optionSeletedborough')
    selectedCrashMarkers = get_coordinates_for_borough(selectedBorough)
    sndmap = Map(
        identifier="sndmap",
        lat=40.7128,
        lng=-74.0060,
        markers=selectedCrashMarkers,
        zoom=11
        #fit_markers_to_bounds = True
    )
    return render_template('./website/map.html', sndmap=sndmap, selectedBorough = selectedBorough, boroughs=boroughs)

if __name__ == "__main__":
    app.run(debug=True)
