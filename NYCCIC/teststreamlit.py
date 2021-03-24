import streamlit as st
import pandas as pd
import plotly.graph_objects as go

csv_file_case = 'cases-by-day.csv'
df= pd.read_csv(csv_file_case,parse_dates=['date_of_interest'])

st.title("Covid19 NYC Data")
st.markdown(
"""
This app is for visualizing the Covid19 data for NYC. 
"""
)

st.markdown("## " + 'Case_Count/Probable_Case_Count')   
st.markdown("#### " +"What Trends would you like to see?")

selected_metrics = st.selectbox(
    label="Choose...", options=['Case_Count','Probable_Case_Count']
)

fig = go.Figure()
if selected_metrics == 'Case_Count':
    fig.add_trace(go.Scatter(x=df.date_of_interest, y=df.Case_Count,
                    mode='lines',
                    name='Case_Count'))
if selected_metrics == 'Probable_Case_Count':
    fig.add_trace(go.Scatter(x=df.date_of_interest, y=df.Probable_Case_Count,
                        mode='markers', name='Probable_Case_Count'))

st.plotly_chart(fig, use_container_width=True)