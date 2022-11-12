'''
Descripción de la API: Esta api nos da información acerca de una bebida 
Nombre: Mariana Canchola Ramírez 
Fecha de creación: 08 noviembre 2022
'''

#Añadí los módulos para agregarle la funcionalidad
import urllib.parse
import requests

#FORMACIÓN DE MI API
url = "https://api.nutritionix.com/v1_1/search/pizza?"
appId = "ffd5f3c6"
appKey ="076f7595c3dd563a6aa6d66df2f5f41f"
query = "Medium pizza"

#Ciclo que le ayuda al usuario a salir cuando lo decida con la palabra "Salir" o "s"
while True:
    query= input("Tamaño: ")
    if query == "Salir" or query == "s":
        break

    url = url + urllib.parse.urlencode({"query":query,"search": query,"appId": appId, "appKey":appKey})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data['hits'][0]["fields"]["item_name"]
    
    for elem in json_data["hits"]:
        if query in elem["fields"]["item_name"]:
            print("Tamaño pizza: " + str(elem["fields"]["item_name"]) )
            print("ID:   " + str(elem["_id"]))
            
if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n") 
    print("Directions from " + (url))