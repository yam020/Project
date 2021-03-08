import altair 
import folium 
import pandas as pd
import numpy 
import requests 

# import the data 
df = pd.read_csv("https://raw.githubusercontent.com/nychealth/coronavirus-data/master/trends/caserate-by-modzcta.csv"
				,header=None)
response = requests.get(url="https://data.cityofnewyork.us/resource/pri4-ifjk.json")
data = pd.json_normalize(response.json())
data = data.loc[:, ['modzcta','pop_est', 'the_geom']]

# combine these two data (convert the rate)

# use the packages to generate the graphs 

