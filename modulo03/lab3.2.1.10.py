'''
Descripción: La declaración break atascado en un ciclo
Autor: Mariana Canchola Ramírez
Fecha: 27 sep 2022
'''

userWord=input("Ingrese una palabra: ")
userWord=userWord.upper()

for letra in userWord:
    if letra=="A":
        continue
    elif letra=="E":
        continue
    elif letra=="I":
        continue
    elif letra=="O":
        continue
    elif letra=="U":
        continue
    else:
        print(letra)