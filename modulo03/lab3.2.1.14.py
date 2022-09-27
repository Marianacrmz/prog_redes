'''
Descripción: Fundamentos del bucle while
Autor: Mariana Canchola Ramírez
Fecha: 27 sep 2022
'''


blocks = int(input("Ingresa el número de bloques: "))

height = 0
while blocks > height:
    height = height + 1
    blocks = blocks - height

print("La altura de la pirámide:", height)
