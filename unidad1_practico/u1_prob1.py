'''
Descripción: Jugando con listas
Escribir un programa que almacene las asignaturas de un curso en una lista, pregunte al usuario la nota
que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje: 
En <asignatura> has sacado <nota> donde <asignatura> es cada una de las asignaturas de la
lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
Autor: Mariana Canchola Ramírez
Fecha: 11 octubre 2022
'''

print ("Bienvenido, ingresa las calificaciones que obtubiste")

#Creamos una lista con las materias
mi_lista = ["Conexion de redes", "Programación de Redes", "Electronica para IdC", "Inglés"] 
#Creamos la variable y lista vacia de las calificaciones que ingresará el usuario
calificaciones = []

#Con una función insertamos las materias en la lista para que nos arroje un texto con cada una de las materias.
for materias in mi_lista:
    calificacion = input("¿Qué calificación sacaste en " + materias + "?\n")
    calificaciones.append(calificacion) #Agregamos un append para que el usuario ingrese la calificación y se almacenen en la lista llamada "calificacion"
for i in range(len(mi_lista)): #Coloqué un range, con la variable i, para que me cree una secuencia de la lista de las materias
    print("\nEn " + mi_lista[i] + " has sacado " + calificaciones[i]) #Finalmente imprimo la materia, con el nombre de cada una de las materias, y su calificación.