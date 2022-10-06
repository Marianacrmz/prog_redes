'''
Descripción: Raíces de la ecuación cuadrática
Autor: Mariana Canchola Ramírez
Fecha: 06 octubre 2022
'''

from math import sqrt
a = int(input("Ingrese a"))
b = int(input("Ingrese b"))
c = int(input("Ingrese c"))
x1= 0
x2= 0
if ((b**2)-4*a*c) < 0:
  print("La solución es: ")
else:
  x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
  x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
  print(x1)
  print(x2)
  