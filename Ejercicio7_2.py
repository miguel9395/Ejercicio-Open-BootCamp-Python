####Ejercicio 7-2 Miguel Zabala######

import time as t

hora = t.strftime('%H') 
minutos = t.strftime('%M') 

if int(hora) >= 19:
	print ("Ya es Hora de Ir a Casa") 
else:
	print ("Faltan {} horas y {} minutos para irse a casa".format(18- int(hora), 59-int(minutos)))
