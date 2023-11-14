import requests
import json
import pandas as pd

from dotenv import load_dotenv
import os
load_dotenv()
account_key = os.getenv('ACCOUNT_KEY')

entries = []
while True:  # Start of the outer loop
    i = 0
    findNextBus = "null"
    busNumber = str(input("What bus to find? "))
    directionNumber = int(input("Which direction? (1 or 2): "))

    while i < 25500:  # To find i number of results 
        payload = {'AccountKey': 'account_key','accept': 'application/json'}
        BusRouteUrl = f'http://datamall2.mytransport.sg/ltaodataservice/BusRoutes?$skip={i}'
        r = requests.get(BusRouteUrl, headers=payload)
        jsonData = r.json()
        findSpecificBus = [entry for entry in jsonData["value"] if entry["ServiceNo"] == busNumber and entry["Direction"] == directionNumber]

        if not findSpecificBus:
            i += 500
        else:
            for entry in findSpecificBus:
                # To print individual JSON output
                print(json.dumps(entry, indent=4))

                entries.append({
                    "BusStopCode": entry["BusStopCode"],
                    "Distance": entry["Distance"]

                })

                df = pd.DataFrame(entries)

            df['Bus Service'] = busNumber
            df['Direction'] = directionNumber
            df['Distance from origin'] = df['Distance']

            # Blank Column
            df[''] = ''

            # Computing Bus Stop Pairs
            bus_stop_pairs = [f"{df['BusStopCode'].iloc[i-1]}-{df['BusStopCode'].iloc[i]}" if i > 0 else '' for i in range(len(df))]
            df['Bus Stops Pairs'] = bus_stop_pairs

            # Computing Distance Between
            df['Distance Between'] = df['Distance'].diff()

            # To Shift Cells 1 Row UP
            df['Bus Stops Pairs'] = df['Bus Stops Pairs'].shift(-1)
            df['Distance Between'] = df['Distance Between'].shift(-1)

            # Inputting data into each columns
            df = df[['Bus Service', 'Direction', '', 'BusStopCode', 'Distance from origin', '', 'Bus Stops Pairs', 'Distance Between']]

            
            # Creating Excel File
            df.to_excel(f"busNumber:{busNumber}_directionNo:{directionNumber}.xlsx", index=False)
            print("Excel File has been created!")

            findNextBus = str(input("Find next bus? (Y or N): "))
            if findNextBus.upper() == "Y":
                break  # Exit the inner loop and re-enter the outer loop
            else:
                i = 999999999  # To end the inner while loop as bus has been found

    if findNextBus == "null":
        print("The bus or direction selected probably doesn't exist.")
        findNextBus = str(input("Find next bus? (Y or N): "))
    elif findNextBus.upper() != "Y":
        break  # To end the outer loop if the answer is not "Y"