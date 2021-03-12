## Project Goal
It is clear to me from the proposal.md file that the goal for the project, which is to provide clear mappings of COVID cases in the NYC area, can be accomplished with Python using the specified packages.

## Data
It is clear that the data will be loaded from the NYC DOH, then parsed to only contain the zip code and other relevant data points based on what the user hovers over/chooses to display.

## Code
The current code includes a proper skeleton for starting this project, which shows the percent positive for COVID across different NYC zip codes.
Some individual functions that could be written to accomplish parts of this goal are:
- Cleaning the data
- Graphing the data
- Mapping the data
- Displaying the data through the REST calls.

## Contributions + Ideas
I think overall, the skeleton code was a great start! It was great to be able to see how the map worked through an example. I also got a general idea of how the classes were meant to be split.

### Contributions
There are a few things that I changed in the package:
- The example file contained all of the skeleton code in one block at the bottom, and I separated these to prevent the file from becoming too cluttered.

- I noticed that data cleaning was happening under the Map class, but I felt that it made more sense to have in the Data class.

- Some of the naming is very specific (i.e. The string "percpos" is used many times as a reference to the percent positive column). I changed these strings to be capitalized and separated into what made the most sense per file. I feel like this will help a lot when using autocomplete, and if a name is changed in one file, it will automatically be changed in other places as well. You can see these constants in data.py; I put them here, because this is where the data parsing and selection occurs.

- I slightly modified the REST calls to be more modular. Instead of just going to /map for the percent positive info, the user puts in map/percpos, map/deathrate, etc. I think that this will help with splitting up the different necessities for map display and calculations.

- There were a few imports that weren't needed in some files. I think after splitting the classes into separate files, the following breakdown makes the most sense:
    - app.py: has imports for FastAPI, uvicorn, and the local class Map. This file deals with what the user will directly see, so I felt that it should only have REST calls and Map to display the map. This might also include Trend in the future, but that can be flexible.
    - data.py: has import for pandas. I kept this library because it deals directly with dataframe manipulation. It loads the data, then provides a clean copy of the data on-demand. I feel like this could be changed to just store the cleaned dataframe in the class, but this can be flexible.
    - map.py: has import for folium, the local class Data and its respective constants. This file deals only with constructing the map based on data.
    - trend.py: has import for altair, numpy, the local class Data and its respective constants. This file deals with calculating different numbers from the data and displaying it in a table.

### Ideas
- When I first go to the map, it shows the entire US. Is there an option to auto-zoom to just NYC?
- If you look in Map and Data, you can see I added self.data_type and self.type, respectively. However, this is based on the assumption that you're not combining multiple data points into one map (i.e. putting death rate and percent positive on the map at the same time). If this is the case, then you might want to make a list for your map (self.data_types, self.types) and add methods like overlay for Map and combine_data for Data.
- Instead of having the message be a JSON on the "/" route, you could make a few buttons to click on to redirect to the different maps.