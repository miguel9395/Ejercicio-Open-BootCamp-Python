#####Ejercicio 6 - 2 Miguel Zabala#####

class Alumno:
    
    def datos(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
 
 
    
    def resultado(self):
               print("Nombre: ",self.nombre)
               print("Nota: ",self.nota)
 
 
    
    def evaluacion(self):
            if self.nota < 3:
                print("El alumno ha suspendido")
            else:
                print("El alumno ha aprobado")
 
 
alumno=Alumno()

alumno.datos(input('Nombre: ',),float(input('Nota: ', )))

alumno.resultado()
alumno.evaluacion()
#####Fin Ejercicio######