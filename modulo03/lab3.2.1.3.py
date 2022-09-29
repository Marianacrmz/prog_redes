'''
Descripción: Bucle con while
Autor: Mariana Canchola Ramírez
Fecha: 27 sep 2022
'''

secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

number = int (input("Adivina el número secreto: "))
while secret_number != number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    number = int (input("Ingresa otro número: "))
print("¡Bien hecho, muggle! Eres libre ahora")
    