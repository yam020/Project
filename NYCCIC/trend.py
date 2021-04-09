import altair as alt
from NYCCIC.covid_data import Data 

class Trend:

    def __init__(self, datatype, zipcode):
        self.data = Data(datatype)
        self.zipcode = zipcode
        self.df_clean = self.data.get_all_data()

    def convert(self, string):
        string = string.replace(' ', '')
        zipcode_list = list(string.split(','))
        return zipcode_list

    def trendmap(self):
        df_clean = self.df_clean
        zipcodels = self.convert(self.zipcode)
        selected_data = df_clean[df_clean['Zipcode'].isin(zipcodels)]
        interval = alt.selection_interval()
        circle = alt.Chart(selected_data).mark_circle().encode(
            x='Date:O',
            y='Zipcode',
            tooltip=['Zipcode', 'Date', 'Case'],
            color=alt.condition(interval, 'Zipcode', alt.value('lightgray')),
            size=alt.Size('Case:Q',
                           scale=alt.Scale(range=[0, 1000]),
                           legend=alt.Legend(title='Case Per 100,000 People')
               ) 
            ).properties(
                   width=1000,
                   height=300,
                   selection=interval
            ).interactive()
       
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