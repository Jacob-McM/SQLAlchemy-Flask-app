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

# How to utilize the Flask server API

---

## 
