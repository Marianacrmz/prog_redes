"""
Descripción: Below the API status print command, add print statements that display the 
from and to locations, as well as the formattedTime, distance, and fuelUsed keys.
Parse and Display Trip Data
Test Metric Conversion
Convert Imperial to Metric
Test Formatting Decimal Places

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

       
    
    