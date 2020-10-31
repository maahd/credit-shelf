from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

from fetch import get_coordinates_for_borough

crashMarkers = get_coordinates_for_borough("QUEENS")

app = Flask(__name__, template_folder=".")
GoogleMaps(app)

@app.route("/")
def mapview():
    # creating a map in the view
    sndmap = Map(
        identifier="sndmap",
        lat=40.7128,
        lng=-74.0060,
        markers=crashMarkers,
        fit_markers_to_bounds = True
    )
    return render_template('./website/map.html', sndmap=sndmap)

if __name__ == "__main__":
    app.run(debug=True)
