from fastapi import FastAPI
import uvicorn
from fastapi.responses import HTMLResponse

from .map import Map

# create the app as an instance of the fastAPI class
app = FastAPI()

# load the database once when the server starts

# create a root endpoint that provide basic information about the webapp
@app.get("/")
def root():
	return {"message": """Go to /map/DATA_TYPE to see the map with its respective type. The current types available are percpos, deathrate, and casert."""}

# create another endpoint for displaying the trend graph
#@app.get("/trend")

# create another endpoint for displaying the map 
# Just try out 
# Codes will be more refined later 
@app.get("/map/{data_type}", response_class=HTMLResponse)
def map(data_type: str):
	m = Map(data_type)
	m = m.map()
	return m._repr_html_()
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
