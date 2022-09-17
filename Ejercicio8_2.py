import pickle

class Vehiculo:
    marca = ""
    precio = ""

    def __init__(self, marca, precio): 
        self.marca = marca
        self.precio = precio
    def __str__(self): 
        return self.marca + '' + self.precio
    
m1 = Vehiculo('Renault', '3000')

f = open('registro_vehiculos.bin', 'wb') 

pickle.dump(m1, f)
f.close()