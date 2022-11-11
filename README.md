# Flask API utilizing SQLAlchemy queries to sqlite database

---

## What is this?

A repo utilizing Flask to call SQLAlchemy queries and display relevant information called from the app. Also Contains an analytical jupyter notebook.

In this repo you will find:

|Notebook| Description|
|--------|------------|
|[Database Analysis Notebook](hawaii_database_analysis.ipynb)| A notebook containing the analysis of the sqlite database. Utilizes SQLAlchemy queries to pull data, pandas to clean and organize, and matplotlib to visualize.|

|Scripts| Description|
|-------|------------|
|[Flask App](app.py)| Python script for flask server and app setup. Calls SQLAlchemy queries based on input URL.|

|Data|Description|
|----|-----------|
|[SQLite Database](hawaii.sqlite)| A SQLite database engine file containing data on hawaii weather station reports.
|[Measurement Data](/Resources/hawaii_measurements.csv)| CSV Containing date-wise measurement data for a given station, the date it recorded data, the precipitation for that date, and the observed temperature|
|[Weather Station Data](/Resources/hawaii_stations.csv)| CSV containing metadata on the stations found in the [Measurement Data](/Resources/hawaii_measurements.csv). The metadata includes the station, its name, its latitude and longitude, and its elevation. 

## What does this repo use?

Seperated by file, these are the dependencies needed to run either the app.py script for the Flask server, or to run the Jupyter Notebook. This project utilized a virtual enviroment that holds all dependencies. 

|app.py Script| Version|
|--------|------------|
|[Flask](https://flask.palletsprojects.com/en/1.1.x/installation/)|1.1.2|
|[SQLAlchemy](https://docs.sqlalchemy.org/en/14/)|1.4.32|

|Jupyter Notebook||Version|
|[Matplotlib](https://matplotlib.org/) |3.5.1|
|[NumPy](https://numpy.org/)|1.21.5|
|[pandas](https://pandas.pydata.org/)|1.4.2|
|[SQLAlchemy](https://docs.sqlalchemy.org/en/14/)|1.4.32|
|[IPython](https://ipython.org/)|8.2.0|
|[Jupyter Notebook](https://jupyter.org)|6.4.8|

Running on Python 3.8.13

# How to utilize the app.py in this repo

---

1. Ensure you have the proper dependencies to run the script, listed above. This project when created utilized a virtual enviroment to load dependencies, which was named PythonData38. If using a virtual envrioment, the first step is to open a terminal/command line from the repo folder and activate the enviroment. E.g `source activate PythonData38`.  

2. Next, type `python app.py`. This will run the python scrip containing the flask server setup. In your terminal/command line you should see `*Serving Flask app "app"`. At the bottom of the asterisk denoted list of information, you should see `Running on <address>` and the key-press needed to close the flask server.

3.  Take the address, which should be `http://<local host address>:<port>/` and type it into your browser window. This project was tested and debugged while using Google Chrome, but the final version has been tested on 


## 
