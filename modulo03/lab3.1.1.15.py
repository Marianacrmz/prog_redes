'''
Descripción: Fundamentos de la sentencia if-elif-else
Autor: Mariana Canchola Ramírez
Fecha: 27 sep 2022
'''

year = int(input("Introduce un año:"))

if year < 1582:
    print ("No dentro del período del calendario Gregoriano")
elif year % 4 != 0:
    print("Año Común")
elif year % 100 != 0:
    print ("Año Bisiesto")
elif year % 400 != 0:
    print("Año Común")
else:
    print ("Año Bisiesto")