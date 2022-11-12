'''
Descripción de la API: API utilizada para personajes del anime.
Nombre: Mariana Canchola Ramírez 
Fecha de creación: 08 noviembre 2022
'''

import requests
personajes = "Gitama"
json_status = 0


url = "https://api.jikan.moe/v4/top/anime"
data = requests.get(url)
if data.status_code == 200:
    data = data.json()
    for e in data["data"]:
        print (e["title"])

while True:
    personajes = input("Personaje correcto: ")
    print (e["title"])
    if personajes == "Salir" or personajes == "s":
     break
 
if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n") 
    print("Directions from " + (url))
