# New York City Covid-19 Interactive Charts (NYCCIC)
### In development 
The project aims to create a webapp to visualize the Covid-19 data in New York City by zipcode. 

### Why I chose this for my project? 
The inspiration comes from my own experience in renting apartment during the pandemic. One thing I considered when renting is the pandemic status of the neighborhoods. There are two websites help me a lot during the process. One is from New York Times. And the other is from New York Gov. However, for the New York Gov website, users can't visualize the Covid-19 data by zipcode (except hospitalizaion and death). It is not very friendly to people who are totally new to the city. (like myself)  For the New York Times, it contains detailed information and beautiful graphs, but requires subscription. (No offense. The New York Times is amazing. I just don't read news that much.)

### Project goal 
Currently, there are many Covid-19 data available online. My main goal is to use this data and create a webapp that can visualize these data in New York City by zipcode. By creating this webapp, I hope I can collect many aspects of Covid-19 data and group them by zipcodes. Meanwhile, I hope I can present a clear and beautiful visulaziation of Covid-19 data, so people can gain a clear understanding of the pandemic status and how pandemic affects areas of New York city differently. As a conclusion, I hope this webapp can help people raise their awareness of Covid-19 in their own community. Though the pandemic cases are falling, we should still stay vigilant. 

### Future goal 
To do list: 
1. Add comment and doc string for my codes (Priority)
2. Made my project looks pretty and easy to use - Streamlit (Streamlit)


 
### Intended Use
#### Install the Packages
```bash
conda install altair -c conda-forge 
conda install folium -c conda-forge
git clone "https://github.com/yam020/NYCCIC.git"
cd ./NYCCIC
pip install -e . 
```
#### Open the webapp 
```bash
cd ./NYCCIC 
uvicorn app:app --reload
```

