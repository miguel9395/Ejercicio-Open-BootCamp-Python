a = open('ejercicio8.txt', 'w')
a.write('Hola aca escribo yo\n')
a.close()

b = open('ejercicio8.txt', 'r')

lectura= b.readline()

print(lectura)
b.close()