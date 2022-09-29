'''
Descripción: Operando con listas - conceptos básicos
Autor: Mariana Canchola Ramírez
Fecha: 29 sep 2022
'''

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

nueva_lista = my_list

for i in my_list:
    if i in nueva_lista:
        del my_list[1]
        
print("La lista con elementos únicos:")
print(my_list)