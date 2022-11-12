
## Import dependancies dependencies
import datetime as dt
import sqlalchemy

## Import functions needed to run queries
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

## Import Flask functions
from flask import Flask, jsonify, request, redirect


# Create Engine
engine = create_engine("sqlite:///resources/hawaii.sqlite")

# New model reflection
Base = automap_base()

# Table reflection
Base.prepare(engine, reflect = True)

# Save references to each table
measurements = Base.classes.measurement
stations = Base.classes.station

## Following instruction, instantiate Flask app.
app = Flask(__name__)


## This function is used to dynamically name the route for the starting date route, as well as anywhere else the start date is needed for queries.

def start():
    session = Session(engine)

    recent_date = session.query(measurements.date).order_by(measurements.date.desc()).first()

    session.close()

    date_str = str(recent_date)
    start_date = date_str.translate({ord(n): None for n in "(,)''"})

    return (start_date)

def last():

    session = Session(engine)

    last = session.query(measurements.date).order_by(measurements.date).first()

    session.close()

    date_str = str(last)
    last_date = date_str.translate({ord(n): None for n in "(,)''"})

    return (last_date)



## The 'Homepage' for the API. Lists the availible routes, and an example URL for the API call that is called for the date range json. 

@app.route("/")
def HomeRoute():
    "Availible API routes"
    
    return(
        f"<b><h1>Availible Routes</b></h1>"
        "<hr>"
        "Shows available routes<br/>"
        f"<code><font size=+2>/api/v1.0/</font></code><br/>"
        "<br/>"
        "<hr>"
        "Calls the precipitation for 1 year from the most recent date in database<br/>"
        f"<code><font size=+2>/api/v1.0/precipitation</font></code><br/>"
        "<br/>"
        "<hr>"
        "Calls the unique stations found in the database<br/>"
        f"<code><font size=+2>/api/v1.0/stations</font></code><br/>"
        "<br/>"
        "<hr>"
        "Calls the observed temperature of the most active station for 1 year from the most recent date in database<br/>"
        f"<code><font size=+2>/api/v1.0/tobs</font></code><br/>"
        "<br/>"
        "<hr>"
        "Calls the average, minimum, and maximum temperature from the dynamically found start of the database until the end.<br/>"
        f"<code><font size=+2>/api/v1.0/<start>{last()}</font></code><br/>"
        "<br/>"
        "<hr>"
        "Calls the average, minimum, and maximum temperature from the user inputed URL date parameters. Example below.<br/>"
        f"<code><font size=+2>/api/v1.0/date_range?start=<i>yyyy-mm-dd</i>&end=<i>yyyy-mm-dd</i></font></code><br/>"
        "<br/>"

        f"<b>Date Range URL Example</b>:<code> api/v1.0/date_range?start=<b>2017-08-23</b>&end=<b>2016-08-23</code></b><br/>"
        "<hr>"
        "<br/>"
        f"Brings the user to the github repo README. Requires an internet connection."
        "<br/>"
        f"<code><font size=+2>/api/v1.0/README</code></font>"
    )

## Alternate route that returns to the availible routes from just the bare API url.

@app.route("/api/v1.0/")
def qol():
    return HomeRoute()

## Route that redirects to the github repo README for this project. 

@app.route("/api/v1.0/README")
def readme():
    return redirect("https://github.com/Jacob-McM/SQLAlchemy-Flask-app/blob/main/README.md")

## Route created for the precipitation json. Contains the query needed to get precipitation data from the database. Essentially the same as the query used in the analysis notebook without the date filter.

## After analysis of the rubric rather than the README, I've re-added the date filter. ## Rubric Language: "Returns the jsonified precipitation data for the last year in the database
                                                                                       ## README Language: "Convert the query results to a dictionary using date as the key and prcp as the value."
                                                                                       # "based on the queries that you have just developed" leaves too much ambiguity in this context, in my opinion

@app.route("/api/v1.0/precipitation")
def percipitation():
    
    session = Session(engine)

    """Returns percipitation and date"""

    ## Construction of date filter

    start_date =  dt.datetime.strptime(start(),'%Y-%m-%d')
    year = dt.timedelta(days=365)
    end = start_date - year
    end = dt.datetime.strftime(end,'%Y-%m-%d')    

    ## Precipitation query

    prcp_date_results = session.query(measurements.date, measurements.prcp).filter(func.strftime("%Y-%m-%d",measurements.date) >= end).all()

    session.close()

    ## For loop to create list for jsonify function to create JSON for route.   

    prcp_dict = {}

    for date,prcp in prcp_date_results:
        prcp_dict[date] = prcp

    return jsonify(prcp_dict)

## Route that will return a list of the stations, their ID, and their 'name' which contains their location.

@app.route("/api/v1.0/stations")
def station():

    session = Session(engine)

    """Returns all unique stations"""

    ## Unique query that doesn't really appear in the analysis notebook. Contains station ID for easy reference, the station itself, and the station 'name' which contains locale contexual information.

    unique_station = session.query(stations.id, stations.station,  stations.name).\
    group_by(stations.station).all()

    session.close()

 ## For loop to create list for jsonify function to create JSON for route.

    stations_list = []

    for id,station,name in unique_station:
        station_dict = {}
        station_dict['B. id'] = id
        station_dict['A. station'] = station
        station_dict['C. name'] = name
        stations_list.append(station_dict)

    return jsonify(stations_list)

## Temperature observation route. Contains the same query as found in the analysis notebook, that being the past year of temperature data for the most active station. 

@app.route("/api/v1.0/tobs")
def temperature():
    
    session = Session(engine)

    """Returns temperature for past year of data in dataset at the most active station"""

    ## Date query and date range construction

    start_date =  dt.datetime.strptime(start(),'%Y-%m-%d')
    year = dt.timedelta(days=365)
    end = start_date - year
    end = dt.datetime.strftime(end,'%Y-%m-%d')
    

    station_counts = session.query(measurements.station, func.count(measurements.id)).\
    group_by(measurements.station).order_by(func.count(measurements.prcp).desc()).all()

    most_active = str(station_counts[0])
    active_station = most_active.split(',')[0]
    active_station = active_station.translate({ord(n): None for n in "(,)''"})
    active_station

    temp_results = session.query(measurements.tobs).\
    filter(func.strftime("%Y-%m-%d",measurements.date) >= end).filter(measurements.station == active_station).all()

    session.close()

    tobs = [tuple(row) for row in temp_results]

    return jsonify(tobs)

## Alternate tobs route with version of query that returns the active station and the date. 
## As the instructions just asked for 'Return a JSON list of temperature observations (TOBS) for the previous year.' My other query for just temperature is used by default, 
## though I think this one offers legibility and assurance of the station. 
## To utilize this version, comment out above @app.route("api/v1.0/tobs") -> return jsonify(tobs), and uncomment below code until return jsonify(tobs_list). 
## One or the other MUST be commented out, or the app will fail due to an AssertionError.  

# @app.route("/api/v1.0/tobs")
# def temperature():
    
#     session = Session(engine)

#     """Returns temperature for past year of data in dataset at the most active station"""

#     ## Date query and date range construction

#     start_date =  dt.datetime.strptime(start(),'%Y-%m-%d')
#     year = dt.timedelta(days=365)
#     end = start_date - year
#     end = dt.datetime.strftime(end,'%Y-%m-%d')
    

#     station_counts = session.query(measurements.station, func.count(measurements.id)).\
#     group_by(measurements.station).order_by(func.count(measurements.prcp).desc()).all()

#     most_active = str(station_counts[0])
#     active_station = most_active.split(',')[0]
#     active_station = active_station.translate({ord(n): None for n in "(,)''"})
#     active_station

#     temp_results = session.query(measurements.tobs, measurements.station, measurements.date ).\
#     filter(func.strftime("%Y-%m-%d",measurements.date) >= end).filter(measurements.station == active_station).all()

#     session.close()

#     tobs_list = []
    
#     for temp,station,date in temp_results:
#         tobs_dict = {}
#         tobs_dict['temperature'] = temp
#         tobs_dict['station'] = station
#         tobs_dict['date'] =  date
#         tobs_list.append(tobs_dict)

#     return jsonify(tobs_list)

######## END OF  /api/v1.0/tobs VARIATION. 


## Route for the displayed json of the average, maximum, and minimum temperature values from the start of the database*, really just all of the temperature data.
## The URL is created dynamically based on a function that queries for the start date of the database when called. 

@app.route(f"/api/v1.0/{last()}")
def allDates():

    session = Session(engine)

    all_temp_results = session.query(func.avg(measurements.tobs),func.max(measurements.tobs),func.min(measurements.tobs)>= last).all()

    session.close()

    stats_list = []

    for avg,max,min in all_temp_results:
        stats_dict = {}
        stats_dict["average"] = avg
        stats_dict["maximum"] = max
        stats_dict['minimum'] = min
        stats_list.append(stats_dict)

    return jsonify(stats_list)


## Route that, based on user inputed URL parmeters, calls the average, maximum, and minimum temperature for the date range found in the parameters. 

@app.route("/api/v1.0/date_range", methods=['GET'])
def dateRange():

    ## Create api call arguments, setting the parameters to be passed into the query. Therefore, following `<URL>?`
    ## start=<start>. 

    args = request.args
    start = args.get('start')
    end = args.get('end')

    ## Find delta between the url param dates
            
    delta1 =  dt.datetime.strptime(start,'%Y-%m-%d')
    delta2  = dt.datetime.strptime(end,'%Y-%m-%d')
    delta =  delta1 - delta2

    session = Session(engine)

    range_results = session.query(func.avg(measurements.tobs),func.max(measurements.tobs),func.min(measurements.tobs)).filter(func.strftime("%Y-%m-%d",measurements.date) >= delta1 - delta).all()


    session.close()

    range_list = []

    for avg,max,min in range_results:
        stats_dict = {}
        stats_dict["average"] = avg
        stats_dict["maximum"] = max
        stats_dict['minimum'] = min
        range_list.append(stats_dict)

    return jsonify(range_list)
   



# # URL Example: /api/v1.0/date_range?start=2017-08-23&end=2016-08-23

if __name__ == '__main__':
    app.run(debug=True)