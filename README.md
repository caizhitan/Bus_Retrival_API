# LTA_DataMall_Analytics

This program is writen in Python using pandas and requests library to fetch data from LTA's Datamall API for data analytics and calculations. 

This program can currently calculate & find for each Bus Service for all/single directions: (As of. Nov 2023)
1. Distance from origin for each Bus Stop.
2. Distance between each Bus Stop Pairs.

(Do note that the code in the repo **DOES NOT contain the authorisation key** please head to `https://datamall.lta.gov.sg/content/datamall/en.html` to request your personal authorisation key.)

## Postman to retrive API Results.
<img width="1515" alt="image" src="https://github.com/caizhitan/Bus_Retrival_API/assets/150103035/054151dd-faa7-4207-8d0f-497bb3ca5e26">

As we can see the API call gives us a list of infomation in this JSON Format:

<img width="218" alt="image" src="https://github.com/caizhitan/Bus_Retrival_API/assets/150103035/1328be07-cc66-4c24-a638-68fb3f54090e">

We are interested in retrieving `"ServiceNo", "Direction", "BusStopCode", "Distance".`

## Writing our Python Code.
Firstly import the necessary libaries. 

<img width="158" alt="image" src="https://github.com/caizhitan/Bus_Retrival_API/assets/150103035/643a58a3-b149-4601-b232-7a5f04098af3">
