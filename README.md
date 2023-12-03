# LTA_DataMall_Analytics

This project is writen in Python using libaries such as Pandas, Numpy, Matplotlib for Data Analytics. 

## This documentation will be split into 2 sections: 
### Data Processing 
- Collecting our Dataset.
- Understanding our Dataset.
- Cleaning our Dataset.
- Transforming our Dataset.
### Data Analysis
- Performing analysis.
- Visualise with graphs.
- Share findings and summary.

# Data Processing
## Collecting our Dataset.
#### Passenger Volume By Train Stations (Dataset #1)
![Dataset #1](https://github.com/caizhitan/LTA_DataMall_Analytics/assets/150103035/79d3914c-744f-4438-9f43-a85ffa311803)


#### Passenger Volume By Origin Destination Train Station (Dataset #2)
![Dataset #2](https://github.com/caizhitan/LTA_DataMall_Analytics/assets/150103035/b14c832b-4416-426d-84b1-38fa8a8f574e)

As the documentation states, Annex A & Annex B tell us about our dataset. 

We can retrieve our dataset by sending a Request Qurey Parameter: `Date=YYYYMM`


# Understanding our Dataset.

### Annex A (Dataset #1)
| YEAR_MONTH | DAY_TYPE | TIME_PER_HOUR | PT_TYPE | PT_CODE | TOTAL_TAP_IN_VOLUME | TOTAL_TAP_OUT_VOLUME |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 2018-05 | WEEKDAY  | 15 | TRAIN | EW14-NS26 | 56019 | 37614 |
| 2018-05 | WEEKENDS/HOLIDAY | 15 | TRAIN | EW14-NS26 | 13385 | 10878 |

### Annex B (Dataset #2)
| YEAR_MONTH | DAY_TYPE | TIME_PER_HOUR | PT_TYPE | ORIGIN_PT_CODE | DESTINATION_PT_CODE | TOTAL_TRIPS |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 2018-05 | WEEKDAY  | 17 | TRAIN | CC28 | CC1-NE6-NS24 | 111 |
| 2018-05 | WEEKENDS/HOLIDAY | 17 | TRAIN | CC28 | CC1-NE6-NS24 | 39 |

# Cleaning our Dataset.
#### Writing our Python Code
#### Import required libraries 
```Python
import pandas as pd
```



# Transforming our Dataset.
