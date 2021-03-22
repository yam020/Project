import folium
from covid_data import Data 

class Map:
    # write different functions to generate different map graphs 
    def __init__(self, string):
        self.GEO = "https://raw.githubusercontent.com/nychealth/coronavirus-data/master/Geography-resources/MODZCTA_2010_WGS1984.geo.json"
        self.data = Data(string)
        self.data_type = string

    def map(self):
        if self.data_type == PERCPOS:
            # data cleanup for percentage postive 
            df_percpos_clean = self.data.get_clean_data()
            m = folium.Map(location=[48, -102], zoom_start=3)
            folium.Choropleth(
                geo_data=self.GEO,
                name="choropleth",
                data=df_percpos_clean,
                columns=[ZIP_CODE, PERCPOS],
            key_on=f"feature.properties.{ZIP_CODE}",
                fill_color="YlGn",
                fill_opacity=0.7,
                line_opacity=0.2,
                legend_name="Percentage postive (%)",
            ).add_to(m)
            folium.LayerControl().add_to(m)
        elif self.data_type == CASERT:
            pass
        elif self.data_type == DEATHRATE:
            pass
        return m # map object