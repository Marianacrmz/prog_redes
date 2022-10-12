'''
Descripción: Día del año: escribiendo y utilizando tus propias funciones
 escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes) 
 y devuelve el día correspondiente del año, o devuelve None si cualquiera de los argumentos no es válido.
Autor: Mariana Canchola Ramírez
Fecha: 04 octubre 2022
'''


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

def days_in_month(year, month):
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year) and month == 2:
            return 29
    return monthDays[month - 1]
#En esta parte del código asignamos una variable para sumarizarla.
def day_of_year(year, month, day):
    if year < 1582:
        return None
    if month > 12 or month < 1:
        return None
    if day > days_in_month(year, month) or day < 1:
        return None
        
    totalDays = day #iguala el total de días para asignarla a una nueva variable
    month = month - 1
    while month > 0:
        totalDays += days_in_month(year, month) #al total de días le sumará el año y meses, y lo devolverá en cifras.
        month -= 1
        
    return totalDays #Devuelve sumando el total de días.

print(day_of_year(2001, 2, 28)) #aqui podemos cambiar este parametro para ver que fecha queremos verificar.
