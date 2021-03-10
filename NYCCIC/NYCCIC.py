import altair 
import folium 
import pandas as pd
import numpy 
import requests 

# import the data 
# case rate by modzcta
caserate = "https://raw.githubusercontent.com/nychealth/coronavirus-data/master/trends/caserate-by-modzcta.csv"
df_caserate = pd.read_csv(caserate, header=None)
# death rate by modzcta
deathrate = "https://raw.githubusercontent.com/nychealth/coronavirus-data/master/trends/deathrate-by-modzcta.csv"
df_deathrate = pd.read_csv(deathrate, header = None)
# percentage positive by modzcta 
percpos = "https://raw.githubusercontent.com/nychealth/coronavirus-data/master/trends/percentpositive-by-modzcta.csv"
df_percpos = pd.read_csv(percpos, header = None)
# geoJson data
geo = "https://raw.githubusercontent.com/nychealth/coronavirus-data/master/Geography-resources/MODZCTA_2010_WGS1984.geo.json"

# use the folium to generate the map 
# data cleanup for percentage postive 
df_percpos_clean = df_percpos.copy()
columnname = df_percpos[:1].values.flatten().tolist()
columnname = [i.replace('PCTPOS_','') for i in columnname if 'PCTPOS_' in i]
columnname.insert(0,'date')
df_percpos_clean.columns = columnname
df_percpos_clean = df_percpos_clean.drop(['CITY','BX','BK','MN','QN','SI'],axis=1)
df_percpos_clean = df_percpos_clean.tail(1).reset_index(drop=True)
df_percpos_clean = df_percpos_clean.T
date = df_percpos_clean.iloc[0,0]
df_percpos_clean = df_percpos_clean.iloc[1:]
df_percpos_clean = df_percpos_clean.reset_index()
df_percpos_clean.columns = ['modzcta','percpos']
df_percpos_clean['percpos'] = pd.to_numeric(df_percpos_clean['percpos'], errors='ignore')
m = folium.Map(location=[48, -102], zoom_start=3)

folium.Choropleth(
    geo_data=geo,
    name="choropleth",
    data=df_percpos_clean,
    columns=["modzcta", "percpos"],
    key_on="type",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Percentage postive (%)",
).add_to(m)

folium.LayerControl().add_to(m)


