# LTA_DataMall_Analytics
### (This project is currently work in progress.)
This program is writen in Python using pandas and requests library to fetch data from LTA's Datamall API for data analytics and calculations. 

This program can currently calculate & find for each Bus Service for all/single directions: (As of. Nov 2023)
1. Distance from origin for each Bus Stop.
2. Distance between each Bus Stop Pairs.

(The code **DOES NOT contain the authorisation key** please head to [https://datamall.lta.gov.sg/content/datamall/en.html](url) to request your personal authorisation key.)



## Understanding the API Documentation.
### API Responses Pages
<img width="973" alt="SCR-20231112-cjfs" src="https://github.com/caizhitan/LTA_DataMall_Analytics/assets/150103035/a7adbf79-6a23-4c27-a102-59ef82d71a4f">

In this section of the documentation, it is worth mentioning that each page contains a fixed amount of data. Therefore, it might be necessary to navigate through multiple pages.

### Bus Route API Description
<img width="973" alt="image" src="https://github.com/caizhitan/LTA_DataMall_Analytics/assets/150103035/fb80b9cf-cca9-416c-ba3e-68eb36217a93">

Here we can see the values we can retrieve by calling the Bus Routes API.



## Postman to retrive API Results.
<img width="1515" alt="image" src="https://github.com/caizhitan/Bus_Retrival_API/assets/150103035/054151dd-faa7-4207-8d0f-497bb3ca5e26">

As we can see the API call gives us a list of infomation in this JSON Format exactly like the documentation:
```JSON
{
            "ServiceNo": "10",
            "Operator": "SBST",
            "Direction": 1,
            "StopSequence": 1,
            "BusStopCode": "75009",
            "Distance": 0,
            "WD_FirstBus": "0500",
            "WD_LastBus": "2300",
            "SAT_FirstBus": "0500",
            "SAT_LastBus": "2300",
            "SUN_FirstBus": "0500",
            "SUN_LastBus": "2300"
        },
```

We are interested in retrieving:
```JSON
 "ServiceNo"
 "Direction"
 "BusStopCode"
 "Distance"
```

## Writing the Python Code.
### Importing libraries required
We are using 3 libraries for this projects: requests, json & pandas.
```Python
import requests
import json
import pandas as pd
```

### Declaring the variables
We are using `entries` to store our data in an array for our Excel Spreadsheet & `previousDirection` to check if the bus route has multiple directions.
```Python
entries = []
previousDirection = None
```

### Handling page skipping if not found
By using a while loop, our program can continue looping until it finds the user-selected bus number or the next 500 results.
```Python
while True:  # Start of the outer loop
    i = 0
    findNextBus = "null"
    busNumber = str(input("What bus to find? "))

    while i < 25500:  # To find i number of results
        payload = {'AccountKey': '[Insert Authorisation Key]',
                   'accept': 'application/json'}
        BusRouteUrl = f'http://datamall2.mytransport.sg/ltaodataservice/BusRoutes?$skip={i}'
        r = requests.get(BusRouteUrl, headers=payload)
        jsonData = r.json()
        findSpecificBus = [entry for entry in jsonData["value"]
                           if entry["ServiceNo"] == busNumber]

        if not findSpecificBus:
            i += 500
```

