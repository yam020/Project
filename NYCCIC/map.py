#!/usr/bin/env python

""" map docstring.
 This script is used to construct map based on the reuqest from the users
 Inside the script, it contains one class.
 This script requires that `folium`, `json`,`request`, `NYCCIC.covid_data` be installed within the
 Python environment you are running this script in.
"""

# import the necessary packages
import json
import folium
import requests
from NYCCIC.covid_data import Data



class Map:
    """
    A class to create map based on user's requests
    ...
    Attributes
    ----------
    string: str

    Methods
    -------
    geojson_tooltop(string, dataframe):
        add tooltip (desired messgae) to the dataframe and return
        Parameters
        ----------
        string: string, required
        dataframe: dataframe, required

        Returns
        -------
        The revised dataframe
    basic_map(response, df_clean, legend_name):
        Parameters
        ----------
        string: string, required
        df_clean: dataframe, required
        legend_name: string, required

        Returns
        -------
        A map object
    map():
        Parameters
        ----------
        None

        Returns
        -------
        The map object
    """
    def __init__(self, string):
        # create a object for Data
        self.data = Data(string)
        # access the geo
        self.geo = "https://raw.githubusercontent.com/nychealth/coronavirus-data/master/Geography-resources/MODZCTA_2010_WGS1984.geo.json"
        # store the data
        self.data_type = string
        # call the function in Data object
        self.df_clean = self.data.get_clean_data()
        # store the json after adding the tooltip
        self.response = self.geojson_tooltip(self.data_type, self.df_clean)

    def geojson_tooltip(self, string, dataframe):
        """
        Load the data based on the requests from users, also append the tooltip to the json

        Parameters
        ----------
        string, required
        dataframe, required

        Returns
        -------
        Geojson data that has tooltip appended
        """
        # load the geodata
        response = json.loads(requests.get(self.geo).text)
        # prepare the customised text
        tooltip_text = []
        # format the text properly based on the string type
        if string == 'PERCPOS':
            for idx in range(len(dataframe)):
                tooltip_text.append(dataframe['modzcta'][idx]+': '+str(dataframe[string][idx])+'%')
        elif string == 'CASERT' or 'TESTRT' or 'HOSPRT' or 'DEATHRT':
            for idx in range(len(dataframe)):
                tooltip_text.append(dataframe['modzcta'][idx]+ \
                                        ': '+str(dataframe[string][idx])+' Case')
        # Append a tooltip column with customised text
        for idx in range(len(tooltip_text)):
            response['features'][idx]['properties']['tooltip'] = tooltip_text[idx]
        return response

    # create the basic map
    def basic_map(self, response, df_clean, legend_name):
        """
        Create the basic map form based on the json, the cleaned data
        and the correct legend name

        Parameters
        ----------
        response, required
        df_clean, required
        legend_name, required

        Returns
        -------
        A map object
        """
        # create the basic map based on json and cleaned data and the legend name
        basicmap = folium.Map(location=[40.7128, -73.9352], zoom_start=10, tiles="cartodbpositron")
        choropleth = folium.Choropleth(
            geo_data=response,
            name="choropleth",
            data=df_clean,
            columns=["modzcta", self.data_type],
            key_on=f"feature.properties.MODZCTA",
            fill_color="OrRd",
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name=legend_name
        ).add_to(basicmap)
        folium.LayerControl().add_to(basicmap)
        # add the tooltip
        choropleth.geojson.add_child(
            folium.features.GeoJsonTooltip(['tooltip'], labels=False)
        )
        return basicmap

    # create the map
    def map(self):
        """
        Specifiy which datatype to use and create the legend name and map

        Parameters
        ----------
        None, Self

        Returns
        -------
        A map object
        """
        # check the datatype and created the legend name. Call the function basic_map to
        # create the map
        if self.data_type == "PERCPOS":
            # legend name
            legend_name = "Percentage Positive %"
            # create the map
            basicmap = self.basic_map(self.response, self.df_clean, legend_name)
        elif self.data_type == "CASERT" or "TESTRT" or "HOSPRT" or "DEATHRT":
            # legend name
            legend_name = "Case Per 100,000 People"
            # create the map
            basicmap = self.basic_map(self.response, self.df_clean, legend_name)
        # return the map object
        return basicmap
