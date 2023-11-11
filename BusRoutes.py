import requests
import json
import pandas as pd

entries = []
previousDirection = None
while True:  # Start of the outer loop
    i = 0
    findNextBus = "null"
    busNumber = str(input("What bus to find? "))

    while i < 25500:  # To find i number of results
        payload = {'AccountKey': '',
                   'accept': 'application/json'}
        BusRouteUrl = f'http://datamall2.mytransport.sg/ltaodataservice/BusRoutes?$skip={i}'
        r = requests.get(BusRouteUrl, headers=payload)
        jsonData = r.json()
        findSpecificBus = [entry for entry in jsonData["value"]
                           if entry["ServiceNo"] == busNumber]

        if not findSpecificBus:
            i += 500

        else:
            for entry in findSpecificBus:
                if previousDirection == 1 and entry['Direction'] == 2:
                    entries.extend([
                        {
                            "BusStopCode": "",
                            "Distance": None,
                            "Direction": "",
                            "Bus Service": None
                        },
                        {
                            "BusStopCode": "",
                            "Distance": None,
                            "Direction": "",
                            "Bus Service": None
                        }
                    ])
                # To print individual JSON output
                print(json.dumps(entry, indent=4))

                entries.append({
                    "ServiceNo": entry["ServiceNo"],
                    "BusStopCode": entry["BusStopCode"],
                    "Distance": entry["Distance"],
                    "Direction": entry["Direction"]
                    
                })
                
                previousDirection = entry["Direction"]
                df = pd.DataFrame(entries)

                
            df["Bus Service"] = df["ServiceNo"]
            df['Distance from origin'] = df['Distance']

            # Blank Column
            df[''] = ''

            # Computing Bus Stop Pairs
            bus_stop_pairs = [f"{df['BusStopCode'].iloc[i-1]}-{df['BusStopCode'].iloc[i]}" if i > 0 and df['BusStopCode'].iloc[i-1] and df['BusStopCode'].iloc[i] else '' for i in range(len(df))]
            df['Bus Stops Pairs'] = bus_stop_pairs
            
            # Computing Distance Between
            df['Distance'] = df['Distance'].astype(float)
            df['Distance Between'] = df['Distance'].diff()

            # To Shift Cells 1 Row UP
            df['Bus Stops Pairs'] = df['Bus Stops Pairs'].shift(-1)
            df['Distance Between'] = df['Distance Between'].shift(-1)

            # Inputting data into each columns
            df = df[['Bus Service', 'Direction', '', 'BusStopCode',
                     'Distance from origin', '', 'Bus Stops Pairs', 'Distance Between']]

            # Handle NaN values
            df['Bus Stops Pairs'].fillna('', inplace=True)

            # Creating Excel File
            df.to_excel(f"busNumber:{busNumber}.xlsx", index=False)
            print("Excel File has been created!")

            findNextBus = str(input("Find next bus? (Y or N): "))
            if findNextBus.upper() == "Y":
                entries = []
                break  # Exit the inner loop and re-enter the outer loop
            else:
                i = 999999999  # To end the inner while loop as bus has been found

    if findNextBus == "null":
        print("The bus or direction selected probably doesn't exist.")
        findNextBus = str(input("Find next bus? (Y or N): "))
        entries = []
    elif findNextBus.upper() != "Y":
        break  # To end the outer loop if the answer is not "Y"