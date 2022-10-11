'''
Descripción: Partiendo fecha
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
Autor: Mariana Canchola Ramírez
Fecha: 11 octubre 2022
'''

print ("Bienvenido\n")

mes = {1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto", 9:"Septiembre", 10:"Octubre", 11:"Noviembre", 12:"Diciembre"}
print ("Escribe tu fecha de nacimiento en formato dd-mm-aaaa")
str = input("Dime cuando naciste: ")

str = str.split('-')

print("Tu naciste el: ",str[0], "de", mes[int(str[1])], "de", str[2])