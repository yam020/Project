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
@app.get("/", response_class=HTMLResponse)
def root():
    """
    create a root endpoint that provide information about the webapp

    Parameters
    ----------
    None

    Returns
    -------
    HTML
    """
    return """
    <html>
        <head>
            <title>Welcome to NYCCIC!</title>
        </head>
        <body>
            <h1> Welcome to NYCCIC! </h1>
            <p style="text-align: center;"> This website aims to provie the visulization of COVID-19 data in NYC by Zipcode. 
            <br />If you want to see the map, go to /map.
            <br />If you want to see the trend graphs, go to /trend.
            <br /> <em />Please note these are case sensitive. </p>
        </body>
    </html>
    """

# create endpoint for displaying the map
@app.get("/map", response_class=HTMLResponse)
def map():
    """
    create a endpoint for map that provide instructions

    Parameters
    ----------
    None

    Returns
    -------
    HTML
    """
    return """
    <html>
        <head>
            <title>Map Options</title>
        </head>
        <body>
            <h1> Map options </h1>
            <p> There are several types of map you can see. 
            <br />If you want to see the percentage postive map, got to /PERCPOS. 
            <br />If you want to see the death rate map, go to /DEATHRT. 
            <br />If you want to see the hospitalized rate map, go to /HOSPRT. 
            <br />If you want to see the test rate map, go to /TESTRT. 
            <br />If you want to see the case rate map, go to /CASERT. 
            <br /> <em />Please note those are case sensitive. </p>
        </body>
    </html>
    """

# create endpoint for displaying the trend graph
@app.get("/trend", response_class=HTMLResponse)
def trend():
    """
    create a endpoint for trend that provide instructions

    Parameters
    ----------
    None

    Returns
    -------
    A html
    """
    return """
    <html>
        <head>
            <title>Trend Graph Options</title>
        </head>
        <body>
            <h1> Trend Graph options </h1>
            <p> There are several types of trend graphs you can see. 
            <br />If you want to see the death rate trend graphs, go to /DEATHRT. 
            <br />If you want to see the hospitalized rate trend graphs, go to /HOSPRT. 
            <br />If you want to see the test rate trend graphs, go to /TESTRT. 
            <br />If you want to see the case rate trend graohs, go to /CASERT. 
            <br /> <em />Please note those are case sensitive. </p>
        </body>
    </html>
    """

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
@app.get("/trend/{data_type}", response_class=HTMLResponse)
def trend_data():
    """
    create a endpoint for trend that provide instructions

    Parameters
    ----------
    None

    Returns
    -------
    A html
    """
    return """
    <html>
        <head>
            <title>Enter the Zipcodes</title>
        </head>
        <body>
            <h1> Enter the zipcodes </h1>
            <p> Please specify the zipcodes you would like to see. 
            <br /> For example,
            <br /> /11201,10001,10002,10005.
            <br /> <em />Please note there should be no space between zipcodes</p>
        </body>
    </html>
    """

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
