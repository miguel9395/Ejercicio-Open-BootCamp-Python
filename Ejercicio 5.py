########Ejercicio 5 Miguel Zabala########

### año bisiesto es divisibleen 4 y 100 y 400

ano = int(input("Escribe el Año:" ,))


def anobisiesto(ano):
     
    if ano % 400 == 0 or (ano % 4 ==0 and ano % 100 != 0) :
        print(ano, 'Es Año Bisiesto')
    else:
         print(ano, 'No es Año Bisiesto')

anobisiesto(ano)
    

###Fin Ejercicio###