#!/usr/bin/env python

""" covid_data docstring.
 This script allows the users to import data from the destined website and clean the data by
 request. Inside the script, it contains one class.
 This script requires that `pandas` be installed within the Python
 environment you are running this script in.
"""


#import package
import pandas as pd


class Data:
    """
    A class to import data from the website and clean the data by requests.
    ...
    Attributes
    ----------
    string: str

    Methods
    -------
    load_data():
        get the data from webstie based on the requests from the user
    get_clean_data():
        clean up the data for the map
    get_all_data():
        clean up the data for the trendgraph
    changetodate(date):
        reformate the data column
        Parameters
        ----------
        date: string, required

        Returns
        -------
        A reformat string

    """
    def __init__(self, string):
        #initialize the storedata
        self.storeddata = pd.DataFrame()
        #store the website address as baseurl
        self.baseurl = "https://raw.githubusercontent.com/nychealth/coronavirus-data/master/trends/"
        #store the input string
        self.type = string
        #load data
        self.load_data()

    def load_data(self):
        """
        Load the data based on the requests from users

        Parameters
        ----------
        None, self

        Returns
        -------
        A dataframe
        """
        # check which datatype users would like to have
        if self.type == "CASERT":
            url_string = f"{self.baseurl}caserate-by-modzcta.csv"
        elif self.type == "PERCPOS":
            url_string = f"{self.baseurl}percentpositive-by-modzcta.csv"
        elif self.type == "DEATHRT":
            url_string = f"{self.baseurl}deathrate-by-modzcta.csv"
        elif self.type == "TESTRT":
            url_string = f"{self.baseurl}testrate-by-modzcta.csv"
        elif self.type == "HOSPRT":
            url_string = f"{self.baseurl}hosprate-by-modzcta.csv"
        # if the input from user does not match any, raise error
        else:
            raise Exception(f"{self.type} is not a valid type for the map.")
        # store the data to the storeddata
        self.storeddata = pd.read_csv(url_string, header=None)

    def get_clean_data(self):
        """
        Clean the data based on the requests from users for the map display

        Parameters
        ----------
        None, self

        Returns
        -------
        A cleaned dataframe
        """
        # make a copy
        df_clean = self.storeddata.copy()
        # fill the missing values with 0
        df_clean = df_clean.fillna(0)
        # get the columnnames from the dataframe
        columnname = df_clean[:1].values.flatten().tolist()
        # Based on each dataype, remove the letters in the columns
        if self.type == "PERCPOS":
            columnname = [i.replace('PCTPOS_', '') for i in columnname if 'PCTPOS_' in i]
        elif self.type == "CASERT":
            columnname = [i.replace('CASERATE_', '') for i in columnname if 'CASERATE_' in i]
        elif self.type == "TESTRT":
            columnname = [i.replace('TESTRATE_', '') for i in columnname if 'TESTRATE_' in i]
        elif self.type == "DEATHRT":
            columnname = [i.replace('DEATHRATE_', '') for i in columnname if 'DEATHRATE_' in i]
        elif self.type == "HOSPRT":
            columnname = [i.replace('HOSPRATE_', '') for i in columnname if 'HOSPRATE_' in i]
        # rename the fist column name data
        columnname.insert(0, 'date')
        # used the modifed column name
        df_clean.columns = columnname
        # drop the columns and transpose
        df_clean = df_clean.drop(df_clean.columns[[0, 1, 2, 3, 4]], axis=1) \
                        .tail(1).reset_index(drop=True).T
        # remove the unwanted and rest the index
        df_clean = df_clean.iloc[1:].reset_index()
        # rename the columnes
        df_clean.columns = ["modzcta", self.type]
        # change the datatype to the numeric
        df_clean[self.type] = pd.to_numeric(df_clean[self.type], errors='ignore')
        # return the cleaned dataframe
        return df_clean

    def changetodate(self, date):
        """
        Reformate the column/datafrmae

        Parameters
        ----------
        string

        Returns
        -------
        A reformated string
        """
        # split the string by "/""
        reformeddate = date.split('/')
        # based on the different data type
        if len(reformeddate) == 3:
            # reformate
            reformeddate = str(reformeddate[2]+'-'+reformeddate[0]+'-'+reformeddate[1])
        if len(reformeddate) == 2:
            # reformate
            reformeddate = str(reformeddate[1]+'-'+reformeddate[0])
        #return the reformated column
        return reformeddate

    def get_all_data(self):
        """
        Clean the data based on the requests from users for the trend graph display

        Parameters
        ----------
        None, self

        Returns
        -------
        A cleaned dataframe
        """
        # make a copy
        df_clean = self.storeddata.copy()
        # get the columnnames from the dataframe
        columnname = df_clean[:1].values.flatten().tolist()
        # Based on each dataype, remove the letters in the columns
        if self.type == "CASERT":
            columnname = [i.replace('CASERATE_', '') for i in columnname if 'CASERATE_' in i]
        elif self.type == "TESTRT":
            columnname = [i.replace('TESTRATE_', '') for i in columnname if 'TESTRATE_' in i]
        elif self.type == "DEATHRT":
            columnname = [i.replace('DEATHRATE_', '') for i in columnname if 'DEATHRATE_' in i]
        elif self.type == "HOSPRT":
            columnname = [i.replace('HOSPRATE_', '') for i in columnname if 'HOSPRATE_' in i]
        # rename the fist column name data
        columnname.insert(0, 'date')
        # used the modifed column name
        df_clean.columns = columnname
        # drop the unwanted columns
        df_clean = df_clean.drop(df_clean.columns[[1, 2, 3, 4]], axis=1)
        # drop one row
        df_clean = df_clean.iloc[1:]
        # group by date
        df_clean = df_clean.melt(id_vars=['date'])
        # create new columnname
        colname = ['Date', 'Zipcode', 'Case']
        # use the new column name
        df_clean.columns = colname
        # change the Date column to the string type
        df_clean['Date'] = df_clean['Date'].astype(str)
        # use the changetodate function to reformat the string
        for i in range(len(df_clean)):
            df_clean['Date'][i] = self.changetodate(df_clean['Date'][i])
        # return the cleaned dataframe
        return df_clean
