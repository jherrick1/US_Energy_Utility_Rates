# US_Energy_Utility_Rates
Access the Streamlit app to visualize US energy utility rates: [here](https://jherrick1-us-energy-utility-rates-main-n1g8y9.streamlit.app/)

(NOTE: the app might take a second to 'wake up' if it has been a while since it has been accessed)

## Introduction


## Data
The data for this project was pulled from the US Energy Information Administration (EIA) website, [here](https://www.eia.gov/electricity/data.php#sales).
There are multiple files on this page, but the data that was used specifically was under: 'Sales (consumption), revenue, prices & customers' > Annual > 'By sector, by state, by provider' (available in xls format).
The original data has also been included in data folder.


## Approach
### Data Preprocessing
The original data was in xls format and utilized subheaders that--while beneficial in a business setting--was not ideal for visualization. To fix this issue, I utilized Excel's built in power query tool to unpivot and reorganize columns. I applied this process to each of the tabs in the original xls which produced the individual csv files in the data folder.
### App Design
After the data was cleaned and ready for use, I started with identifying which columns could be utilized for graph inputs. These were: state, year, sector, provider, count type. Based on those, I added the appropriate UI widgets to the app so the user could adjust a line graph and the contents it displays.

The first three (state, year, sector) are included on a sidebar which adjust the line graph parameters, while the other two (provider, count type) allows the user to select the contents of the graph.
### Widget Options
- State:
- Year:
- Sector:
- Provider:
- Count Type: 
