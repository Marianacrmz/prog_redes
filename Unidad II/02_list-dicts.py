'''
Descripción: Encontrar el error en el script.
Autor: Mariana Canchola Ramírez
Fecha: 18 octubre 2022
'''



# Create a list of the BRICS countries
country = [ 
            "Brazil", 
            "Russia", 
            "India", 
            "China", 
            "South Africa"
          ]

"""Create a dictionary of BRICS capitals.
Note that South Africa has 3 capitals. Therefore, we embed a list inside
the dictionary.
"""

capitals = {
    "Brazil": "Brasilia",
    "Russia": "Moscow",
    "India": "New Delhi",
    "China": "Beijing",
    "South Africa": [
                        "Pretoria",
                        "Cape Town",
                        "Bloemfontein"
                    ]
           }

# Print the list and dictionary
print( country ) #Quite las comillas para que no se imprimiera el texto sino lo que venía dentro de la cadena.
print( capitals ) #Lo mismo aquí
"""
What response did you get?
Why did the list and dictionary contents not print?
Por que estaba entre comillas.
Fix the code and run the script again.
"""

print(capitals["South Africa"][1]) #Estaba mal escrito para imprimir la segunda capital, ya que no estaban bien cerrados los corchetes. 
"""
Why did you get an error for the 2nd capital of South Africa?   
Hint: Check the syntax for the index value.
"""
