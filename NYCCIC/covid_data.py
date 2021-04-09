import pandas as pd



class Data:
    def __init__(self, string):
        self.storeddata = pd.DataFrame()
        self.baseurl = "https://raw.githubusercontent.com/nychealth/coronavirus-data/master/trends/"
        self.type = string
        self.load_data()

    def load_data(self):
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
        else:
            raise Exception(f"{self.type} is not a valid type for the map.")
        self.storeddata = pd.read_csv(url_string, header=None)

    def get_clean_data(self):
        df_clean = self.storeddata.copy()
        df_clean = df_clean.fillna(0)
        columnname = df_clean[:1].values.flatten().tolist()
        # change the name properly 
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
        columnname.insert(0, 'date')
        df_clean.columns = columnname
        df_clean = df_clean.drop(df_clean.columns[[0, 1, 2, 3, 4]], axis=1) \
                        .tail(1).reset_index(drop=True).T
        df_clean = df_clean.iloc[1:].reset_index()
        df_clean.columns = ["modzcta", self.type]
        df_clean[self.type] = pd.to_numeric(df_clean[self.type], errors='ignore')
        return df_clean

    def changetodate(self, date):
        reformeddate = date.split('/')
        if len(reformeddate) == 3:
            reformeddate = str(reformeddate[2]+'-'+reformeddate[0]+'-'+reformeddate[1])
        if len(reformeddate) == 2:
            reformeddate = str(reformeddate[1]+'-'+reformeddate[0])
        return reformeddate

    def get_all_data(self):
        df_clean = self.storeddata.copy()
        columnname = df_clean[:1].values.flatten().tolist()
        if self.type == "CASERT":
            columnname = [i.replace('CASERATE_', '') for i in columnname if 'CASERATE_' in i]
        elif self.type == "TESTRT":
            columnname = [i.replace('TESTRATE_', '') for i in columnname if 'TESTRATE_' in i]
        elif self.type == "DEATHRT":
            columnname = [i.replace('DEATHRATE_', '') for i in columnname if 'DEATHRATE_' in i]
        elif self.type == "HOSPRT":
            columnname = [i.replace('HOSPRATE_', '') for i in columnname if 'HOSPRATE_' in i]
        columnname.insert(0, 'date')
        df_clean.columns = columnname
        df_clean = df_clean.drop(df_clean.columns[[1, 2, 3, 4]], axis=1)
        df_clean = df_clean.iloc[1:]
        df_clean = df_clean.melt(id_vars=['date'])
        colname = ['Date', 'Zipcode', 'Case']
        df_clean.columns = colname 
        df_clean['Date'] = df_clean['Date'].astype(str)
        for i in range(len(df_clean)):
            df_clean['Date'][i] = self.changetodate(df_clean['Date'][i])
        return df_clean