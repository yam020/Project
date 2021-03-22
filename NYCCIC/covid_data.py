# import packages 
import pandas as pd

CASERT = "casert"
DEATHRATE = "deathrate"
PERCPOS = "percpos"
ZIP_CODE = "MODZCTA"

class Data:
	def __init__(self, string):
		self.df = pd.DataFrame()
		self.BASE_URL = "https://raw.githubusercontent.com/nychealth/coronavirus-data/master/trends/"
		self.type = string
		self.load_data()

	def load_data(self):
		if self.type == CASERT:
			url_string = f"{self.BASE_URL}caserate-by-modzcta.csv"
		elif self.type == PERCPOS:
			url_string = f"{self.BASE_URL}percentpositive-by-modzcta.csv"
		elif self.type == DEATHRATE:
			url_string = f"{self.BASE_URL}deathrate-by-modzcta.csv"
		else:
			raise(f"{self.type} is not a valid type for the map.")
		self.df = pd.read_csv(url_string, header=None)

	def get_clean_data(self):
		# data cleanup for percentage postive 
		df_clean = self.df.copy()
		columnname = df_clean[:1].values.flatten().tolist()
		columnname = [i.replace('PCTPOS_','') for i in columnname if 'PCTPOS_' in i]
		columnname.insert(0,'date')
		df_clean.columns = columnname
		df_clean = df_clean.drop(['CITY','BX','BK','MN','QN','SI'],axis=1) \
						.tail(1).reset_index(drop=True).T
		date = df_clean.iloc[0,0]
		df_clean = df_clean.iloc[1:].reset_index()
		df_clean.columns = [ZIP_CODE, self.type]
		df_clean[self.type] = pd.to_numeric(df_clean[self.type], errors='ignore')
		return df_clean
	