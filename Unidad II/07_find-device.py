'''
Descripción: El usuario ingresa un dispositivo, si hay alguno que se llame como tal que s eimprima si no, enviar un mensaje que diga "Dispositivo no encontrado"
Autor: Mariana Canchola Ramírez
Fecha: 20 octubre 2022
'''

file = open("devices.txt", "r")

for line in file:
    line = line.strip()
    disp = (input("Ingresa el nombre de un dispositivo: ")) 
    if disp in line:
       print(line) 
    else: ("Dispositivo no encontrado")
file.close()