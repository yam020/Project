from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from NYCCIC.map import Map
#from trend import Trend

# create the app as an instance of the fastAPI class
app = FastAPI()

# create a root endpoint that provide basic information about the webapp
@app.get("/")
def root():
    return {"message": """Go to /map or /trend"""} 

# create endpoint for displaying the map 
@app.get("/map")
def root():
    return {"message": """Go to /PERCPOS or /TESTRT or /DEATHRT or /HOSPRT or /CASERT"""} 

# create endpoint for displaying the trend graph
@app.get("/trend")
	return {"message": """Under Construction"""} 

# create endpoint for different data type 
@app.get("/map/{data_type}", response_class=HTMLResponse)
async def map(data_type: str):
    m = Map(data_type)
    m = m.map()
    return m._repr_html_()
