'''
Descripción: Lea un número y despliegue una secuencia de números de N hasta 1.
Autor: Mariana Canchola Ramírez
Fecha: 06 octubre 2022
'''

#Definimos las variables, con un input para que el usuario ingrese dos números al azar que se almacenaran en x y y
x = int(input())
y = int(input()) 

#Colocamos una condición, que nos ayude a determinar si x y y son diblisibles, el cual si es así mostrará un mensaje de que si son divisibles.
def divisible(x, y):
    if x%y == 0: #El simbolo % se usa para obtener el residuo en una división.
        print("El ",x,"es divisible entre ", y)  #Imprime la leyenda si es divisible 
    else:
        print("El ",x,"no es divisible entre ", y)   #usamos un if else por si esta condición no se cumple.
divisible(x, y) 
