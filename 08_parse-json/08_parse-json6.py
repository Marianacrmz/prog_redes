"""
Descripción: Iterate Through the Directions Data
Add an if statement below the double line print statement to check the json_status. 
The for loop iterates through each maneuvers list, prints the narrative, and prints the distance in kilometers formatting for 2 decimal places.
Autor: Mariana Canchola Ramírez
Fecha: 25 octubre 2022
"""

import urllib.parse
import requests

main_api = "http://www.mapquestapi.com/directions/v2/route?key=AcmRjoStpUXGkukz4wDGKXwYy6myo4Zu&from=Clarendon+Blvd,Arlington,VA&to=2400+S+Glebe+Rd,+Arlington,+VA"
key = "AcmRjoStpUXGkukz4wDGKXwYy6myo4Zu"

# The "while true" construct creates an endless loop.
while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break

    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + str(json_data["route"]["formattedTime"]))
        print("Miles:           " + str(json_data["route"]["distance"]))
        print("Fuel(Gal):       " + str(json_data["route"]["fuelUsed"]))
        print("Kilometers:      "+ str("{:.2f}".format((json_data["route"]["distance"]) * 1.61)))
        print("Fuel Used (Ltr): "+ str("{:.2f}".format((json_data["route"]["fuelUsed"]) * 3.78)))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"])+ " ("+ str("{:.2f}".format((each["distance"]) * 1.61) + " km)"))
        print("=============================================\n")
