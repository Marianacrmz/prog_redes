"""
Descripción: Get Your MapQuest API Key, trabajando con MapQuest y las API's
Autor: Mariana Canchola Ramírez
Fecha: 25 octubre 2022
"""

import urllib.parse
import requests

main_api = "http://www.mapquestapi.com/directions/v2/route?key=AcmRjoStpUXGkukz4wDGKXwYy6myo4Zu&from=Clarendon+Blvd,Arlington,VA&to=2400+S+Glebe+Rd,+Arlington,+VA"
orig = "Washington"
dest = "Baltimaore"
key = "AcmRjoStpUXGkukz4wDGKXwYy6myo4Zu"
url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})

json_data = requests.get(url).json()
print(json_data)