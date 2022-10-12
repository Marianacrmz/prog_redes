'''
Descripción: Números primos: ¿Cómo encontrarlos?
Escribir una función que verifique si un número es primo o no.
Autor: Mariana Canchola Ramírez
Fecha: 04 octubre 2022
'''
#utilizamos una variable que el programa ya trae por defecto.
#POr lo cual utilizamos un def para que hagamos las operaciones correspondientes.
def is_prime(num):
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            return False
        divisor += 1 
    return True
            
#Con un for  realizamos un ciclo el cual nos arrojará con las operaciones ya declaradas arriba si es un número primo o no. 
for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
