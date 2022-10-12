'''
Descripción: Lea un número y despliegue una secuencia de números de N hasta 1.
Autor: Mariana Canchola Ramírez
Fecha: 06 octubre 2022
'''

#Creamos una variable, insertamos su tipo y un input para que el usuario introduzca un número al azar
num = int(input("Introduce un número entero que sea positivo: "))
#Para esto hice un ciclo for,en el cual los datos se almacenaran en i, con la condicón de comenzar desde 0 y terminar en n número.
for i in range(num, 0, -1):
    print(i, end=",")
