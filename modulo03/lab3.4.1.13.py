'''
Descripción: Lo básico de las listas - Los Beatles
Autor: Mariana Canchola Ramírez
Fecha: 29 sep 2022
'''

# paso 1
Beatles = []
print("Paso 1:", Beatles)

# paso 2
Beatles.append ("John Lennon")
Beatles.append ("Paul McCartney")
Beatles.append ("George Harrison")
print("Paso 2:", Beatles)

# paso 3
for miembros in range(2):
    Beatles.append (input("El nuevo miembro de la banda es: "))
print("Paso 3:", Beatles)

# paso 4
del Beatles [-1]
del Beatles [-1]
print("Paso 4:", Beatles)

# paso 5
Beatles.insert (0,"Ringo Starr")
print("Paso 5:", Beatles)


# probando la longitud de la lista
print("Los Fav", len(Beatles))
