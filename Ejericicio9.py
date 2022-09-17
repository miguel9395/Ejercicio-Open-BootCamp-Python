datos = input("Introduce países separados por comas:\n")

paises = [pais for pais in datos.split(",")]

print(",".join(sorted(list(set(paises)))))
