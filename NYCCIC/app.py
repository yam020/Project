#!/usr/env/bin python

""" app docstring.
This is the script for the main app. The endpoints were built.
This script requires that `io`, `fastapi`, `NYCCIC.map`, `NYCCIC.trend` be installed within the
Python environment you are running this script in.
"""

# import the required packages
from io import StringIO
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from NYCCIC.map import Map
from NYCCIC.trend import Trend


# create the app as an instance of the fastAPI class
app = FastAPI()

# create a root endpoint that provide basic information about the webapp
@app.get("/")
def root():
    """
    create a root endpoint that provide information about the webapp

    Parameters
    ----------
    None

    Returns
    -------
    A string
    """
    return {"message": """Go to /map or /trend"""}

# create endpoint for displaying the map
@app.get("/map")
def map():
    """
    create a endpoint for map that provide instructions

    Parameters
    ----------
    None

    Returns
    -------
    A string
    """
    return {"message": """Go to /PERCPOS or /TESTRT or /DEATHRT or /HOSPRT or /CASERT"""}

# create endpoint for displaying the trend graph
@app.get("/trend")
def trend():
    """
    create a endpoint for trend that provide instructions

    Parameters
    ----------
    None

    Returns
    -------
    A string
    """
    return {"message": """Go to /TESTRT or /DEATHRT or /HOSPRT or /CASERT"""}


# create endpoint for different data type
@app.get("/map/{data_type}", response_class=HTMLResponse)
async def map_data(data_type: str):
    """
    create a endpoint for map

    Parameters
    ----------
    data_type: string

    Returns
    -------
    A HTML
    """
    # create a map object based on the data type desired
    map_class = Map(data_type)
    # call the function to create the map
    map_display = map_class.map()
    # displat the html of the lab
    return map_display._repr_html_()

# create endpoint for different data type
@app.get("/trend/{data_type}")
def trend_data():
    """
    create a endpoint for trend that provide instructions

    Parameters
    ----------
    None

    Returns
    -------
    A string
    """
    return {"message": """Type desired zipcode- Example:/11201,10001,10002,10005"""}

# create endpoint for different data type based on the zipcode users enter
@app.get("/trend/{data_type}/{zipcode}", response_class=HTMLResponse)
async def trend_data_zip(data_type: str, zipcode: str):
    """
    create a endpoint for trend graphs

    Parameters
    ----------
    data_type: string
    ziocode: string

    Returns
    -------
    A HTML
    """
    # create a trend object
    graph = Trend(data_type, zipcode)
    # get the altair chart
    chart = graph.trendmap()
    # write to HTML string and return
    htmlchart = StringIO()
    chart.save(htmlchart, format='html')
    return htmlchart.getvalue()
