'''
Descripción de la API: API utilizada para ver todos los articulos de Tesla del ultimo año
Nombre: Mariana Canchola Ramírez 
Fecha de creación: 08 noviembre 2022
'''
import urllib.parse
import requests

main_api = "https://newsapi.org/v2/everything?q=tesla&from=2022-10-08&sortBy=publishedAt&apiKey=24a06f6c8b5847b0b5a166e697e43466"

print("URL: " + (main_api))
    
while True:
    respuesta = input("Desea salir? ")
    if respuesta == "Salir" or respuesta == "s":
     break
    
