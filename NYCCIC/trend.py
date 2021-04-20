#!/usr/bin/env python

""" trend docstring.
 This script is used to construct trendgraphs based on the reuqest from the users
 Inside the script, it contains one class.
 This script requires that `altair`, `NYCCIC.covid_data` be installed within the
 Python environment you are running this script in.
"""

# import the necessary packages
import altair as alt
from NYCCIC.covid_data import Data


class Trend:
    """
    A class to create trend graphs based on user's requests
    ...
    Attributes
    ----------
    datatype: str
    zipcode: str

    Methods
    -------
    convert(string):
        Parameters
        ----------
        string: string, required

        Returns
        -------
        A list of zipcode
    trendmap():
        Parameters
        ----------
        None

        Returns
        -------
        The plot object
    """

    def __init__(self, datatype, zipcode):
        # create the data object based on the input
        self.data = Data(datatype)
        # store the zipcode
        self.zipcode = zipcode
        # store the cleaned data
        self.df_clean = self.data.get_all_data()
        # store the datatype
        self.datatype = datatype

    def convert(self, string):
        """
        convert the zipcode input from users to the list

        Parameters
        ----------
        string, required

        Returns
        -------
        List of the zipcodes
        """
        # get rid of the blanck space
        string = string.replace(' ', '')
        # split the string with , and conver to list
        zipcode_list = list(string.split(','))
        # return the list
        return zipcode_list

    def trendmap(self):
        """
        create the trendmap based on the zipcodes and datatype

        Parameters
        ----------
        None, self

        Returns
        -------
        A trendmap plot object
        """
        # create the copy
        df_clean = self.df_clean.copy()
        # convert the string of zipcodes to a list
        zipcodels = self.convert(self.zipcode)
        # select the zipcodes from the graph
        selected_data = df_clean[df_clean['Zipcode'].isin(zipcodels)]
        interval = alt.selection_interval()

        # define the order of the graphs based on input from users
        if self.datatype == "DEATHRT" or "HOSPRT":
            sorteddate = df_clean.iloc[:13, 0].tolist()
        else:
            sorteddate = df_clean.iloc[:36, 0].tolist()
        # create the first graph
        circle = alt.Chart(selected_data).mark_circle().encode(
            x=alt.X('Date', sort=sorteddate),
            y='Zipcode',
            tooltip=['Zipcode', 'Date', 'Case'],
            color=alt.condition(interval, 'Zipcode', alt.value('lightgray')),
            size=alt.Size('Case:Q', scale=alt.Scale(range=[0, 1000]), legend=alt.Legend(title='Case\
                Per 100,000 People'))
            ).properties(
                width=1000,
                height=300,
                selection=interval
            ).interactive()

        # create the second chart
        bars = alt.Chart(selected_data).mark_bar().encode(
            y='Zipcode',
            color='Zipcode',
            x='sum(Case):Q',
            tooltip=['sum(Case):Q'],
        ).properties(
            width=1000
        ).transform_filter(
            interval
        ).interactive()
        return circle & bars
