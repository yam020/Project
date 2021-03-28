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
        self.df_clean = self.data.get_clean_data()
        self.response = self.geojson_tooltip(self.data_type, self.df_clean)

    def geojson_tooltip(self, string, dataframe):
        # geodata
        response = json.loads(requests.get(self.geo).text)
        # prepare the customised text
        tooltip_text = []
        # change the name properly
        if string == 'PERCPOS':
            for idx in range(len(dataframe)):
                tooltip_text.append(dataframe['modzcta'][idx]+': '+str(dataframe[string][idx])+'%')
        elif string == 'CASERT' or 'TESTRT' or 'HOSPRT' or 'DEATHRT':
            for idx in range(len(dataframe)):
                tooltip_text.append(dataframe['modzcta'][idx]+': '+str(dataframe[string][idx])+' Case')
        # Append a tooltip column with customised text
        for idx in range(len(tooltip_text)):
            response['features'][idx]['properties']['tooltip'] = tooltip_text[idx]
        return response

    def basic_map(self, response, df_clean,legend_name):
        # create the basic map 
        m = folium.Map(location=[40.7128,-73.9352], zoom_start=10, tiles = "cartodbpositron")
        choropleth = folium.Choropleth(
            geo_data=response,
            name="choropleth",
            data=df_clean,
            columns=["modzcta", self.data_type],
            key_on=f"feature.properties.MODZCTA",
            fill_color="OrRd",
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name= legend_name
        ).add_to(m)
        folium.LayerControl().add_to(m)
        # tooltip function 
        choropleth.geojson.add_child(
            folium.features.GeoJsonTooltip(['tooltip'], labels=False)
        )
        return m 

    def map(self):
        if self.data_type == "PERCPOS":
            # legend name 
            legend_name = "Percentage Positive %"
            # create the map
            m = self.basic_map(self.response, self.df_clean, legend_name)
        elif self.data_type == "CASERT" or "TESTRT" or "HOSPRT" or "DEATHRT":
            # legend name 
            legend_name = "Case Per 100,000 People"
            # create the map
            m = self.basic_map(self.response, self.df_clean, legend_name)
        # return the map object 
        return m 