'''
Descripción de la API: API utilizada para obtener toda la información posible de Instagram con datos en tiempo real
Nombre: Mariana Canchola Ramírez 
Fecha de creación: 08 noviembre 2022
'''


import requests

url = "https://instagram47.p.rapidapi.com/user_following"

querystring = {"userid":"1718924098"}

headers = {
	"X-RapidAPI-Key": "b406c660c9msh451a383f7a3a0b0p127563jsnd427bf933e3a",
	"X-RapidAPI-Host": "instagram47.p.rapidapi.com"
}


response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)