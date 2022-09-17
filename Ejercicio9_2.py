####Ejercicio 9 - 2########3
from functools import reduce

numeros = [3, 7, 8, 253]



impares = list(filter(lambda x : x % 2 != 0, numeros))
print(impares)

consecutivo = reduce(lambda x, y: x + y, impares)
print(consecutivo)

