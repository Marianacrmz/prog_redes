'''
Descripción: Evaluar o encontrar el tiempo final de un periodo de tiempo dado
Autor: Mariana Canchola Ramírez
Fecha: 22 sep 2022
'''
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

hour=(hour+((mins + dura)//60))%24
mins=((mins + dura)%60)
print(hour,mins,sep=":")