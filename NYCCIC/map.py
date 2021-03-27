import folium
import json
import requests
from NYCCIC.covid_data import Data 



class Map:
    # write different functions to generate different map graphs 
    def __init__(self, string):
        self.data = Data(string)
        self.geo = "https://raw.githubusercontent.com/nychealth/coronavirus-data/master/Geography-resources/MODZCTA_2010_WGS1984.geo.json"
        self.data_type = string

    def geojson_tooltip(self, string, dataframe):
        # geodata
        response = json.loads(requests.get(self.geo).text)
        # prepare the customised text
        tooltip_text = []
        if string == 'percpos':
            for idx in range(len(dataframe)):
                tooltip_text.append(dataframe['modzcta'][idx]+': '+str(dataframe[string][idx])+'%')
        # Append a tooltip column with customised text
        for idx in range(len(tooltip_text)):
            response['features'][idx]['properties']['tooltip'] = tooltip_text[idx]
        return response

    def map(self):
        map_c = Map(self.data_type)
        if self.data_type == "PERCPOS":
            # data cleanup for percentage postive 
            df_percpos_clean = self.data.get_clean_data_percpos()
            # create a basic map 
            m = folium.Map(location=[40.7128,-73.9352], zoom_start=10, tiles = "cartodbpositron")
            # geodata
            response = json.loads(requests.get(self.geo).text)
            response = map_c.geojson_tooltip('percpos', df_percpos_clean)
            choropleth = folium.Choropleth(
                geo_data=response,
                name="choropleth",
                data=df_percpos_clean,
                columns=["modzcta", "percpos"],
                key_on=f"feature.properties.MODZCTA",
                fill_color="OrRd",
                fill_opacity=0.7,
                line_opacity=0.2,
                legend_name="Percentage Postive (%)",
            ).add_to(m)
            folium.LayerControl().add_to(m)
            # tooltip function 
            choropleth.geojson.add_child(
                folium.features.GeoJsonTooltip(['tooltip'], labels=False)
            )
        elif self.data_type == "CASERT":
            df_percpos_clean = self.data.get_clean_data_caserate()
            # create a basic map 
            m = folium.Map(location=[40.7128,-73.9352], zoom_start=10, tiles = "cartodbpositron")
            # geodata
            response = json.loads(requests.get(self.geo).text)
            # prepare the customised text
            tooltip_text = []
            for idx in range(len(df_percpos_clean)):
                tooltip_text.append(df_percpos_clean['modzcta'][idx]+': '+str(df_percpos_clean['casert'][idx])+' Case')
            # Append a tooltip column with customised text
            for idx in range(len(tooltip_text)):
                response['features'][idx]['properties']['tooltip'] = tooltip_text[idx]
            choropleth = folium.Choropleth(
                geo_data=response,
                name="choropleth",
                data=df_percpos_clean,
                columns=["modzcta", "casert"],
                key_on=f"feature.properties.MODZCTA",
                fill_color="OrRd",
                fill_opacity=0.7,
                line_opacity=0.2,
                legend_name="Case Rate Per 100,000 People",
            ).add_to(m)
            folium.LayerControl().add_to(m)
            # tooltip function 
            choropleth.geojson.add_child(
                folium.features.GeoJsonTooltip(['tooltip'], labels=False)
            )
        elif self.data_type == "DEATHRATE":
            pass
        # return the map object 
        return m 