# LTA_DataMall_Analytics

### This project is writen in Python using libaries such as Pandas, Numpy, Matplotlib for Data Analytics. 

## This documentation will be split into 2 sections: 
#### Data Processing 
- Collecting our Dataset.
- Understanding our Dataset.
- Cleaning our Dataset.
- Transforming our Dataset.
#### Data Analysis
- Performing analysis.
- Visualise with graphs.
- Share findings and summary.

## Data Processing
### Collecting our Dataset.
#### API Response Documentation 
#### Train Dataset #1
![Dataset #1](https://github.com/caizhitan/LTA_DataMall_Analytics/assets/150103035/79d3914c-744f-4438-9f43-a85ffa311803)


#### Train Dataset #2
![Dataset #2](https://github.com/caizhitan/LTA_DataMall_Analytics/assets/150103035/b14c832b-4416-426d-84b1-38fa8a8f574e)

As the documentation states, all we need is to send a Request for the date we want and we will get a AWS S3 bucket link for the data. 






## Writing the Python Code for Data Processing.
### Importing libraries required
We are using 3 libraries for this projects: requests, json & pandas.
```Python
import requests
import json
import pandas as pd
```

