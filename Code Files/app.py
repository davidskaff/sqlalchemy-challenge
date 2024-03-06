from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import numpy as np
import datetime as dt

app = Flask(__name__)

@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"Welcome to the Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end"
    )

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Calculate the date one year from the last date in data set
    one_year_ago = dt.datetime.strptime(most_recent_date[0], '%Y-%m-%d') - dt.timedelta(days=365)

    # Query for the date and precipitation for the last year
    precipitation_data = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= one_year_ago).\
        order_by(Measurement.date).all()

    # Dict with date as the key and prcp as the value
    precip = {date: prcp for date, prcp in precipitation_data}
    
    return jsonify(precip)

@app.route("/api/v1.0/stations")
def stations():
    # Query all stations
    stations_data = session.query(Station.station).all()

    # Convert list of tuples into normal list
    stations = list(np.ravel(stations_data))
    
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    # Calculate the date one year from the last date in data set
    one_year_ago = dt.datetime.strptime(most_recent_date[0], '%Y-%m-%d') - dt.timedelta(days=365)

    # Query the dates and temperature observations of the most active station for the last year of data
    tobs_data = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == most_active_station).\
        filter(Measurement.date >= one_year_ago).all()

    # Convert list of tuples into normal list
    tobs = list(np.ravel(tobs_data))
    
    return jsonify(tobs)

@app.route("/api/v1.0/<start>")
def start(start):
    # Query TMIN, TAVG, and TMAX for all dates greater than or equal to the start date
    temp_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()

    # Convert list of tuples into normal list
    temps = list(np.ravel(temp_data))
    
    return jsonify(temps)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    # Query TMIN, TAVG, and TMAX for dates between the start and end date inclusive
    temp_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    # Convert list of tuples into normal list
    temps = list(np.ravel(temp_data))
    
    return jsonify(temps)
