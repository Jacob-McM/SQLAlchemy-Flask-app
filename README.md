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

|Jupyter Notebook|Version|
|--------|------------|
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

3.  Take the address, which should be `http://<local host address>:<port>/` and type it into your browser window. This project was tested and debugged while using Google Chrome. Browser conflicts are not expected, but have not been tested extensively. The app has been tested for and should work on Firefox and Microsoft Edge.

4. You have now launched the app, and should be viewing the avalible route calls avalible. In detail, they are as follows:

|Route URL| Description|
|--------|------------|
|/api/v1.0/|Returns the route list. Intended for convinence, as one can append this to the url and view the routes that can be built from it. The intention is that one can easily just input the suffix from the other routes from the main page. For example, from `<local_address>/api/v1.0/` one could easily append `precipition` to the end for the precipitation route, and only have to worry about removing that suffix.|
|/api/v1.0/precipitation| This calls for the precipitation as queried by SQLAlchemy. The parameters the SQLAlchemy query uses is the precipitation of 1 year of datapoints from the most recent date in the database. |
|/api/v1.0/stations| This calls for the list of stations in the databse as queried by SQLAlchemy. The query pulls the ID of the station, which exists as the Primary Key in the database, the real world ID of the station which is in the format of `USC00xxxxxx` with x being unique numbers, and the name of the station, which contains contexual locale information such as 'Honolulu Observatory' or 'Kualoa Ranch Headquarters'. 
|/api/v1.0/tobs|tobs is assumed to mean `Temperature Observed`, and is the temperature data recorded by a given station. This route calls a query that pulls the tobs data for the dynamically determined most active station. The most active station is defined as the station that has the most row data. Null datapoints were excluded from this consideration. As a final filter, the active stations tobs data is queried for the same date range as the precipitation query, that being the tobs data of 1 year from the most recent database entry.|
|/api/v1.0/2010-01-01| This route will call the average, minimum, and maximum temperature from the last date listed, meaning the very first date inputed. At the time of writing this date is 2010-01-01, and while it is statically input here in the ReadMe, it is dynamically found in the app. This was done more for demonstration purposes, as it is unlikely data would be retroactively added, thus creating a new starting date.|
/api/v1.0/date_range? `start=yyyy-mm-dd&end=yyyy-mm-dd`| This route will run a call based on user inputed URL Parameters. The Parameters are in the code markdown in the route URL here. They are `start=`&`end=`. They must be inputed in the yyyy-mm-dd format as shown, where yyyy is full century year, mm is the zero-padded month, and dd is the zero padded day. For example, `2022-06-21` is a sutible date entry. 06/21/2022 is not. The final URL should look like `/api/v1.0/date_range?start=2015-05-28&end=2015-06-21`. For reference, the range availible for query is `2010-01-01` ~ `2018-8-23` |
|/api/v1.0/README| Directs to this repo and its README. For reference. |


## Notebook Analysis Summary

Also found in this repo is a [Jupyter Notebook](hawaii_database_analysis.ipynb) that utilizes SQLAlchemy to query the included SQLite database file, and utilizes pandas and matplotlib to make dataframe analysis and visualizations from the SQLAlchemy queries. The queries made are mostly similar to the flask app routing calls. The visualizations include a bar plot that quantifies the past year of precipitation data in inches starting from the most recent date in the dataset. This range is from 2016-08-23 ~ 2017-08-23. The second visualization found is a histogram that shows the frequency of observed temperature values from the most activate weather station found in the dataset.


## References/Acknowledgements

###### Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, https://doi.org/10.1175/JTECH-D-11-00103.1
###### © 2022 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
