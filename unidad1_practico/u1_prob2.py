'''
Descripción: Lea un número y despliegue una secuencia de números de N hasta 1.
Autor: Mariana Canchola Ramírez
Fecha: 06 octubre 2022
'''


x = int(input())
y = int(input()) 

def divisible(x, y):
    if x%y == 0:
        print("El ",x,"es divisible entre ", y)
    else:
        print("El ",x,"no es divisible entre ", y)
divisible(x, y)
