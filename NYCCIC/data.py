# import packages 
import numpy
import pandas as pd

CASERT = "casert"
DEATHRATE = "deathrate"
PERCPOS = "percpos"
ZIP_CODE = "MODZCTA"

class Data:

	def __init__(self, string):
		self.df = pd.DataFrame()
		self.BASE_URL = "https://raw.githubusercontent.com/nychealth/coronavirus-data/master/trends/"
		self.load_data(string)

	def load_data(self, string):
		if string == CASERT:
			url_string = f"{self.BASE_URL}caserate-by-modzcta.csv"
		elif string == PERCPOS:
			url_string = f"{self.BASE_URL}percentpositive-by-modzcta.csv"
		elif string == DEATHRATE:
			url_string = f"{self.BASE_URL}deathrate-by-modzcta.csv"
		self.df = pd.read_csv(url_string, header=None)

	def get_clean_data(self):
		# use the folium to generate the map 
		# data cleanup for percentage postive 
		df_percpos_clean = self.df.copy()
		columnname = df_percpos_clean[:1].values.flatten().tolist()
		columnname = [i.replace('PCTPOS_','') for i in columnname if 'PCTPOS_' in i]
		columnname.insert(0,'date')
		df_percpos_clean.columns = columnname
		df_percpos_clean = df_percpos_clean \
							.drop(['CITY','BX','BK','MN','QN','SI'],axis=1) \
							.tail(1).reset_index(drop=True).T
		date = df_percpos_clean.iloc[0,0]
		df_percpos_clean = df_percpos_clean.iloc[1:].reset_index()
		df_percpos_clean.columns = [ZIP_CODE, PERCPOS]
		df_percpos_clean[PERCPOS] = pd.to_numeric(df_percpos_clean[PERCPOS], errors='ignore')
		return df_percpos_clean