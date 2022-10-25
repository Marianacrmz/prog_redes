"""
Descripción: Test Quit Functionality
Run your code script and verify it works.
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
