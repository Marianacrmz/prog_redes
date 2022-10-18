'''
Descripción: Create a program with a while loop that counts to a user’s supplied number.
Autor: Mariana Canchola Ramírez
Fecha: 18 octubre 2022
'''

x=input("Enter a number to count to: ")
x=int(x)
y=1
if x <= 0:
    x=x*-1
    
while y<=x:
    print(y)
    y=y+1
