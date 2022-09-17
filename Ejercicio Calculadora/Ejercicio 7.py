#####Ejercicio 7 Miguel Zabala#####
import Calculadora as ca

####Calculadora####

print("""   Opciones de Calculadora:
            1: Sumar  2: Restar 3: Multiplicar 4: Dividir""")
operacion = input ('Ingrese Una Opcion: ')

a = float(input('Ingrese primer numero: '))
b = float(input('Ingrese segundo numero: '))

if operacion == '1':
    print(ca.sumar(a,b))
elif operacion == '2':
    print(ca.restar(a,b))
elif operacion == '3':
    print(ca.multiplicar(a,b))
elif operacion == '4':
    print(ca.dividir(a,b))
else: print('Escriba una opcion valida')

print('Gracias por usar Calculadora')
