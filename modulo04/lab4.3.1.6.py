'''
Descripción: Un año bisiesto: escribiendo tus propias funciones
Tu tarea es escribir y probar una función que toma un argumento (un año) y devuelve True si el año es un año bisiesto, o False si no lo es.
Autor: Mariana Canchola Ramírez
Fecha: 04 octubre 2022
'''

#Primero realizamos una función que nos servirá para los parametros que nos pide el ejercicio
#Si esta condición es 
def is_year_leap(year):
    if year < 1582:  #Si 1582 es menor que el año almacenado nos devolverá falso
        return False
    elif year % 4 != 0: # esta sentencia la vamos a utilizar para que identifique los años bisiestos
        return False
    elif year % 100 != 0: 
        return True
    elif year % 400 != 0: 
        return False
    else: 
        return True

#Este ciclo verifica si el año es bisiesto o no, y arroja un OK, añadiendo un array para insertar los datos que se verificarán. 
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
