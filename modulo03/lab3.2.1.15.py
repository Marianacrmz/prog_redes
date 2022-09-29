'''
Descripción: Hipótesis de Collatz
Autor: Mariana Canchola Ramírez
Fecha: 29 sep 2022
'''


c0 = int(input("Ingresa un número: "))
if c0 < 1:
   print ("Usa números que no sean negativos")
   exit
steps = 0

while c0 != 1:
    if c0 % 2 == 0:
         c0 = int(c0 / 2)
    else:
         c0 = 3 * c0 + 1
    print(c0)
    steps += 1
print("El total de pasos es: ", steps)