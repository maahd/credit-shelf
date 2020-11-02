# Bicycle Crashes #

I used pipenv for managing my python environment.

Please create a .env file in the project root and fill it with two environment variables. The username and password for your local sql database.
Log into MySQL on the command line and run this command: `CREATE DATABASE credit_shelf`

The documentation relevant to each steps is listed below:

Stage 0) cd into the home dir for the project and run `pipenv shell`. Then run `python forBorough.py`.

Stage 1) run `python insertIntoDatabase.py`

Stage 3) The web app is built with Flask. First run `export FLASK_APP=map.py`. Then `flask run`. Keep in mind that this is a developer preview. It's not free to use the Google Maps API anymore. If the map doesn't load, please run
`pip install flask-googlemaps`.

Version:
Python 3.8.6
Flask 1.1.2
Werkzeug 1.0.1

Blue markers are stations. Green markers are crashes.

I have included a dump of the final state of my database. You can also use my sql python scripts to set up your DB locally and import data into it. For example, you can use createStationTable.sql like this:

`mysql -u <YOUR MYSQL USERNAME HERE> -p credit_shelf < sql/createStationTable.sql`

The `processStationData` dir has the python scripts I used to clean and combine the files for the station data. This data was later imported into the DB.
