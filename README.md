# New York City Covid-19 Interactive Charts (NYCCIC)

### Short Description 
#### Project goal
The project aims to create a webapp to visualize the Covid-19 data in New York City by zipcode. 
Currently, there are many Covid-19 data available online. My main goal is to use this data and create a webapp that can visualize these data in New York City by zipcode. By creating this webapp, I hope I can collect many aspects of Covid-19 data and group them by zipcodes. Meanwhile, I hope I can present a clear and beautiful visulaziation of Covid-19 data, so people can gain a clear understanding of the pandemic status and how pandemic affects areas of New York city differently. As a conclusion, I hope this webapp can help people raise their awareness of Covid-19 in their own community. Though the pandemic cases are falling, we should still stay vigilant. 
#### What users can find in my website? 
In this app, users can either visit the map or the trend graphs.
For map, users can chose among test rate map, hospitalized rate map, death rate map, case rate map and the percentage positive map. 
Map contains the hover effect. When users move their mouse over on the desired area, it will pop out a basic message of the COVID-19 situation in this area. 
For trend graphs, users can chose among test rate graphs, hospitalized rate graphs, death rate graphs and case rate map. 
Users can chose what zipcodes they want to observe. The number of the zipcodes users can type is unlimited. 
The trend graphs have both selection effect and hover effect. 

### How to use my website? 
Open the browser and enter https://nyccic.herokuapp.com/
Or you can click [here](https://nyccic.herokuapp.com/)
Website contains instructions on how to use this webiste. 
#### What if you want to run the codes locally? 
first you have to install the relevent packages and clone my repo
```bash
conda install altair requests pandas fastAPI uvicorn folium -c conda-forge 
git clone "https://github.com/yam020/NYCCIC.git"
cd ./NYCCIC
pip install -e . 
```
Then you can open the webapp 
```bash
cd ./NYCCIC 
uvicorn app:app --reload
```

