'''
Descripción: Convirtiendo el consumo de combustible
La tarea es escribir un par de funciones que conviertan l/100km a mpg (milas por galón), y viceversa.
Autor: Mariana Canchola Ramírez
Fecha: 04 octubre 2022
'''
#Colocamos un def, que es una palabra reservada para crear una condición
def liters_100km_to_miles_gallon(liters):
    gallons = liters / 3.785411784 #el 3.78 equivale a un litro por kilometro
    miles = 100000 / 1609.344  #Y una milla contiene 1609.344
    milpg = miles / gallons #Dividimos las millas entre los galones para que nos retorne nuestro resultado
    return milpg
#Hacemos lo mismo pero para que lo convierta a litros
def miles_gallon_to_liters_100km(miles):
    kilometers = (miles * 1609.344) / 1000
    liters = 3.785411784
    liters_100km = (100 / kilometers) * liters
    return liters_100km
#Cantidades de ejemplo para que nos imprima los resultados esperados.
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
