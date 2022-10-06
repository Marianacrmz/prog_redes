'''
Descripción: Convirtiendo el consumo de combustible
Autor: Mariana Canchola Ramírez
Fecha: 04 octubre 2022
'''

def liters_100km_to_miles_gallon(liters):
    gallons = liters / 3.785411784
    miles = 100000 / 1609.344
    milpg = miles / gallons
    return milpg

def miles_gallon_to_liters_100km(miles):
    kilometers = (miles * 1609.344) / 1000
    liters = 3.785411784
    liters_100km = (100 / kilometers) * liters
    return liters_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
