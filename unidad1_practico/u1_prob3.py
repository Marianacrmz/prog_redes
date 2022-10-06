'''
Descripción: Lea un número y despliegue una secuencia de números de N hasta 1.
Autor: Mariana Canchola Ramírez
Fecha: 06 octubre 2022
'''

num = int(input("Introduce un número entero que sea positivo: "))
for i in range(num, 0, -1):
    print(i, end=",")