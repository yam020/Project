# New York City Covid-19 Interactive Charts
The project aims to create a webapp to visualize the Covid-19 data in New York City by zipcode. 


### In Development 
```bash
conda install altair -c conda-forge 
conda install folium -c conda-forge
conda install altair_viewer -c conda-forge
git clone "https://github.com/yam020/NYCCIC.git"
cd ./NYCCIC
pip install -e . 
```


### Note:
```bash
cd ./NYCCIC 
uvicorn app:app --reload
```

