import estudiante as es

class Egresado(es.Estudiante):
    def __init__ (self, nombreIn, edadIn, idIn, carreraIn, fechaIn, ):
        es.Estudiante.__init__(self, nombreIn, edadIn, idIn, carreraIn, "Egresado de la universidad")
        self.fecha = fechaIn
    def trabajar (self, empresa):
        print (f"Hola soy {self.nombre} y trabajo en {empresa}.")