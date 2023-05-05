# US_Energy_Utility_Rates
Streamlit app to visualize US energy utility rates: here
(NOTE: the app might have take a second to 'wake up' if it has been a while since it has been accessed)

### Introduction


---
### Data
The data for this project was pulled from the US Energy Information Administration (EIA) website, [here](https://www.eia.gov/electricity/data.php#sales).
There are multiple files on this page, but the data that was used specifically was under: 'Sales (consumption), revenue, prices & customers' > Annual > 'By sector, by state, by provider' (available in xls format).
The original data has also been included in data folder.

---
### Approach
## Data Preprocessing
The original data was in xls format and utilized subheaders that--while beneficial in a business setting--was not ideal for visualization. To fix this issue, I utilized Excel's built in power query tool to unpivot and reorganize columns. I applied this process to each of the tabs in the original xls which produced the 
