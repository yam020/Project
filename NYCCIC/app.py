#!/usr/env/bin python

"""
Main web app
"""

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
    return {"message": """Go to /map or /trend"""} 

# create endpoint for displaying the map 
@app.get("/map")
def map():
    return {"message": """Go to /PERCPOS or /TESTRT or /DEATHRT or /HOSPRT or /CASERT"""} 

# create endpoint for displaying the trend graph
@app.get("/trend")
def trend():
    return {"message": """Go to /TESTRT or /DEATHRT or /HOSPRT or /CASERT"""} 


# create endpoint for different data type 
@app.get("/map/{data_type}", response_class=HTMLResponse)
async def map_data(data_type: str):
    map_class = Map(data_type)
    map_display = map_class.map()
    return map_display._repr_html_()


@app.get("/trend/{data_type}")
def trend_data():
    return {"message": """Type desired zipcode- Example:/11201,10001,10002,10005"""}


@app.get("/trend/{data_type}/{zipcode}", response_class=HTMLResponse)
async def trend_data_zip(data_type: str, zipcode: str):
    graph = Trend(data_type, zipcode)

    # get the altair chart
    chart = graph.trendmap()

    # write to HTML string and return
    htmlchart = StringIO()
    chart.save(htmlchart, format='html')
    return htmlchart.getvalue()
