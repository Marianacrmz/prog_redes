'''
Descripción: La sentencia continue - El Bonito Devorador de Vocales
Autor: Mariana Canchola Ramírez
Fecha: 27 sep 2022
'''


word_without_vowels = ""

user_word = input("Ingrese la palabra: ").upper()

for letter in user_word:
    if letter in "AEIOU":
        continue
    word_without_vowels += letter
    
print (word_without_vowels)
