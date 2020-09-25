# Clase 2020/9/23 - Clases y Objetos

class Persona:
    def __init__ (self, nombreIngresado, edadIngresado, idIngresado, estaturaIngresado, pesoIngresado):
        self.raza = "Humana"
        self.nombre = nombreIngresado
        self.edad = edadIngresado
        self.id = idIngresado
        self.estatura = estaturaIngresado
        self.peso = pesoIngresado
        print ("Hola mundo estoy viv@!")
    def caminar (self):
        print ("Voy a caminar.")
    def saludo (self,hi):
        print (hi)

class Biomedico (Persona):
    def cultivarCelulas (self):
        print (f"Hola, soy {self.nombre} y voy a cultivar células.")

class Arquitecto (Persona):
    def dibujarPlanos (self):
        print (f"Hola, soy {self.nombre} y voy a dibujar un plano.")

karla = Arquitecto ("Karla", 19, 1234567890, 1.68, 48)

karla.caminar()

juan = Biomedico ("Juan Pablo", 21, 1122334455, 1.80, 60)

juan.caminar()

karla.saludo ("Holi Crayoli")
juan.saludo ("Hola Coca-Cola")

karla.dibujarPlanos()
juan.cultivarCelulas()