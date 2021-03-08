import json
import pandas as pd
from fastapi import FastAPI
from NYCCIC import ...

# create the app as an instance of the fastAPI class
app = FastAPI()

# load the database once when the server starts

# create a root endpoint that provide basic information about the webapp
@app.get("/")


# create another endpoint for displaying the trend graph
@app.get("/trend")

# create another endpoint for displaying the map 
@app.get("/map")
