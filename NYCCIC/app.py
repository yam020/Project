from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from NYCCIC.map import Map
#from trend import Trend

# create the app as an instance of the fastAPI class
app = FastAPI()

# load the database once when the server starts

# create a root endpoint that provide basic information about the webapp


@app.get("/")
def root():
    return {"message": """Go to /map"""} 


# create another endpoint for displaying the trend graph
#@app.get("/trend")

# create another endpoint for displaying the map 
# Just try out 
# Codes will be more refined later 
@app.get("/{data_type}", response_class=HTMLResponse)
async def map(data_type: str):
    m = Map(data_type)
    m = m.map()
    return m._repr_html_()
