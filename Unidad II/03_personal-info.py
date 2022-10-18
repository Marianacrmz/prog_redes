'''
Descripción:Create a script that asks for four pieces of information such as: first name, last name, location, and age.
Create a variable for a space: space = " "
Add a print statement that that combines all the information in one sentence.
Autor: Mariana Canchola Ramírez
Fecha: 18 octubre 2022
'''


#Create a script that asks for four pieces of information such as: first name, last name, location, and age.
name = input("¿Cual es tu primer nombre? ")
lastName = input("¿Cual es tu apellido? ")
loc = input("¿Donde vives? ")
edad = input("¿Cual es tu edad? ")


#Create a variable for a space: space = " "
space = " "


#Add a print statement that that combines all the information in one sentence.
print("Hola " + name + space + lastName + " tu vives en " + loc + " y tienes " + edad + " años")