# Proposal 
## New York City Covid-19 Interactive Charts

### The goal of the project 
The project aims to create a webapp to visualize the Covid-19 data in New York City by zipcode. 

### The reasoning of the project
The inspiration comes from my own experience in renting apartment during the pandemic. One thing I considered when renting is the pandemic status of the neighborhoods. There are two websites help me a lot during the process. One is from [New York Times](https://www.nytimes.com/interactive/2020/us/coronavirus-us-cases.html). And the other is from [New York Gov](https://www1.nyc.gov/site/doh/covid/covid-19-data.page#7day). However, for the New York Gov website, users can't visualize the Covid-19 data by zipcode (except hospitalizaion and death). It is not very friendly to people who are totally new to the city. (like myself)  For the New York Times, it contains detailed information and beautiful graphs, but requires subscription. (The New York Times is amazing. I just don't read news that much.) Currently, there are so many Covid-19 data available online. My main goal is to use this data and create a webapp that can visualize these data in New York City by zipcode. By creating this webapp, I hope I can collect many aspects of Covid-19 data and group them by zipcodes. Meanwhile, I hope I can present a clear and beautiful visulaziation of Covid-19 data, so people can gain a clear understanding of the pandemic status. As a conclusion, I hope this webapp can help people raise their awareness of Covid-19 in their own community. Though the pandemic cases are falling, we should still stay vigilant. 

### Description of the project
The Covid-19 data: case (new/total), death, test, hospitalized, vaccinated.
<br> By entering the desired zipcode/boroughs, users are able to see the trend graphs of Covid-19 case/death/test/hospitalized/vaccinated number in that particular area. The webapp also provides a map of new york that display the new case/total case/tests/vaccine/death in New York City. The map is divided by zipcode. Users can move their mouse over to the interested area to check the Covid-19 situation.

### Description of User interaction 
Users can access the webapp by visiting website: -------. The webapp displays one trend graph and one map. For the trend graphs, users are able to enter the zipcode, or boroughs. Also, users can choose what type of Covid-19 data they want to observe. For the map, users can move their mouse over to their interested ares to check the data. All graphs can be zoom in/out. 
#### Type of data/input a user provide to the program
None

### Description of Data
#### Covid-19 data 
I initially planned to use restAPI to access the data in New York Open Database. With more researching, I found the dataset has no been updated since last December. Instead, I would like to use the Covid-19 data from [NYC health department](https://www1.nyc.gov/site/doh/covid/covid-19-data-totals.page#zip). They stored and updated their data in [github respitories](https://github.com/nychealth/coronavirus-data/tree/master/trends). The webapp uses the latest dataset when users access the webapp. The dataset contains case rate/death rate/hopitalized rate/positive rate/test rate by the zipcode. These data are all in csv format. 

<br> Below is an example for the case rate data by zipcode.

``` Python 
import pandas as pd 
df = pd.read_csv("https://raw.githubusercontent.com/nychealth/coronavirus-data/master/trends/caserate-by-modzcta.csv", header=None)
print(df.head())
```
#### Zipcode and population data
Since the above data shows the rate, it is necessary to use population data to convert to total cases/ or increament of case per se. The zipcode and population data can be accessed through the New York Open Database by using restAPI. The data is in format of JSON. The endpoint is: https://data.cityofnewyork.us/resource/pri4-ifjk.json. 

<br> Below is an example: 

```Python
import requests
response = requests.get(url="https://data.cityofnewyork.us/resource/pri4-ifjk.json")
data= pd.json_normalize(response.json())
data_show = data.loc[:, ['modzcta','pop_est']]
print(data_show.head())
```
#### Geodata
The geodata is same in the [previous section](####Zipcode and population data). 
The data contains the coordinates as well. 

<br> Below is an example: 

```Python
import requests
response = requests.get(url="https://data.cityofnewyork.us/resource/pri4-ifjk.json")
data= pd.json_normalize(response.json())
data_show = data.loc[:, ['modzcta','the_geom']]
print(data_show.head())
```
#### Other info regarding the data
##### Covid-19 data
The dataset is approx. updated in a rate of 7 days. The earliest record is 08/08/2020.
##### Zipcode and population data/ Geodata
The dataset is updated in May 19, 2020. 
> " A shapefile for mapping data by Modified Zip Code Tabulation Areas (MODZCTA) in NYC, based on the 2010 Census ZCTA shapefile. MODZCTA are being used by the NYC Department of Health & Mental Hygiene (DOHMH) for mapping COVID-19 Data. "
> Reference: [NYC Open Data](https://data.cityofnewyork.us/Health/Modified-Zip-Code-Tabulation-Areas-MODZCTA-/pri4-ifjk)

### Output 
Here is a drawing of my final product in my mind. 
![alt text](https://raw.githubusercontent.com/yam020/NYCCIC/main/img/img.png)

### Currently exisiting/similar webapp/websites
There are lots of Covid-19 trackers website existed, such as [New York Times](https://www.nytimes.com/interactive/2020/us/coronavirus-us-cases.html), [New York Gov](https://www1.nyc.gov/site/doh/covid/covid-19-data.page#7day), [JHU](https://coronavirus.jhu.edu/us-map). Those websites are great resources. But in these website, it is very hard to track the coronvarius status by one single zipcode. Even some of the websites contain such information, it lacks visualiztion of these data, e.g. trend graph of Covid-19 in one zipcode. Also, the Covid-19 data by zipcode is relatively scattered. I would like to group them together and create a platform that can visualize these data easily and clearly. 

### Description of the code:
The packages I would like to use in the webapps are the following: 
<br> **folium**: This package is used to generate the map plot. Specifically, I will make a chloropleth map. The [Geodata](####Geodata) will be applied. 
<br> **altair**: This package is used to visualize the data. I chose this one over others simply because it looked nicer for me. The interesting interactive graphs examples are including: interactive legend, multi-line highlight, chloropleth map. I would like to adopted the former two graph type in my webapp.
<br> The two packages below are used to clean, organize and analyze the data. 
<br> **pandas**
<br> **numpy**
<br> **fastAPI** is used to build API. 
