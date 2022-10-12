'''
Descripción: ¿Cuántos días?: escribiendo y utilizando tus propias funciones
escribir y probar una función que toma dos argumentos (un año y un mes) y devuelve 
el número de días del mes/año dado (mientras que solo febrero es sensible al valor year, tu función debería ser universal)
Autor: Mariana Canchola Ramírez
Fecha: 04 octubre 2022
'''

#Esto lo pegamos del laboratorio anterior.
def is_year_leap(year):
    if year < 1582:
        return False
    elif year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else: 
        return True
#Estos son los ultimos días de los meses. los cuales están declarados en un array.
def days_in_month(year, month):
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year) and month == 2:
            return 29
    else:
        return monthDays[month - 1]
#la variable nos da años y días al azar para probar nuestro programa.
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
#Declarado cada uno en su variable correspondiente obtendremos los resultados deseados.
