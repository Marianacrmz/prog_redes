'''
Descripción: Partiendo fecha
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
Autor: Mariana Canchola Ramírez
Fecha: 11 octubre 2022
'''

print ("Bienvenido\n")
#Cree un array para identificar los meses del año y que cada número de mes ingresado por el usuario lo iguale al mes que es. 
mes = {1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto", 9:"Septiembre", 10:"Octubre", 11:"Noviembre", 12:"Diciembre"}
print ("Escribe tu fecha de nacimiento en formato dd-mm-aaaa") 
str = input("Dime cuando naciste: ") #Solicite la fecha de nacimiento al usuario, en el formato dd-mm-aaaa para que las variables se asignen correctamente.

str = str.split('-') #Cada dato irá separado por "-"

print("Tu naciste el: ",str[0], "de", mes[int(str[1])], "de", str[2]) #Imprimí la fecha de nacimiento en conjunto con el array para que me especificara el mes.
