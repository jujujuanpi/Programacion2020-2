# FUNCIONES DE NÚMERO MAYOR

a = int (input ("Ingrese el primer número: "))
b = int (input ("Ingrese el segundo número: "))

def numero (numero1, numero2):
    if a > b:
        print (f"El primer número, {a}, es mayor que el primer número, {b}.")
    elif b > a:
        print (f"El segundo número, {b} es mayor que el primer número, {a}.")
    else:
        print ("Los números son iguales.")

numero (a, b)

# LISTADO DE NOMBRES

nombresLista = []
nombresLista = ["Juan Pablo", "Melany", "Daniel", "Valeria", "Mario", "Karla"]

size = len (nombresLista)

def listado (nombresIngresados):
    for i in range (size):
        print (f"Hola! Soy {nombresLista [i]}.")

listado (nombresLista)

# IMC

peso = int (input ("Ingrese el peso: "))
estatura = float (input ("Ingrese la estatura: "))

def imcFuncion (a, b):
    return round(a / b**2, 3)

imc = imcFuncion (peso, estatura)

print (f"El IMC calculado es de {imc}")

# FUNCIÓN QUE RECIBE OTRA

pesoB = int (input ("Ingrese el peso: "))
estaturaB = float (input ("Ingrese la estatura: "))

def imcs (imcFuncion, a, b):
    imc = imcFuncion (a, b)
    print (f"El IMC calculado es de {imc}")

imcs (imcFuncion, pesoB, estaturaB)

# Clase y Objetos de Personas

class Humanos:
    def __init__ (self, z, y, x, w, v, u):
        self.nombre = z
        self.edad = y
        self.id = x
        self.peso = w
        self.altura = v
        self.sexo = u
        print ("Se ha creado una nueva persona.")
    def atributos (self):
        print (f"Hola! Mi nombre es {self.nombre}, soy de sexo {self.sexo}, tengo {self.edad} años, mi ID es {self.id}, peso {self.peso} kg y mido {self.altura} metros.")

humano1 = Humanos ("Andres", 19, 1122334455, 70, 1.80, "Masculino")
humano2 = Humanos ("David", 23, 5497255, 90, 1.70, "Masculino")
humano3 = Humanos ("Andrea", 21, 57385893, 67, 1.50, "Femenino")

listaAtr = ("Andres", 19, 1122334455, 70, 1.80, "Masculino")
humano1.atributos()
humano2.atributos()
humano3.atributos()

# CLASE HEREDADA

class Estudiante (Humanos):
    def __init__ (self, z, y, x, w, v, u, t, s, r):
        Humanos.__init__(self, z, y, x, w, v, u)
        self.semestre = t
        self.universidad = s
        self.carrera = r
        print ("Se ha creado un nuevo estudiante.")
    def atributoss (self):
        print(f"Hola! Mi nombre es {self.nombre}, soy de sexo {self.sexo}, tengo {self.edad} años, mi ID es {self.id}, peso {self.peso} kg y mido {self.altura} metros. Estudio en {self.universidad} en el {self.semestre} semestre y la carrera {self.carrera}.")
    def clase (self, materia):
        print (f"Hola soy {self.nombre} y voy a asistir a la clase de {materia}.")

estudiante1 = Estudiante ("Maria", 20, 58374, 60, 1.60, "Femenino", 5, "CES", "Ingeniería Biomédica")
estudiante2 = Estudiante ("Jesus", 23, 65392, 70, 1.76, "Masculino", 3, "CES", "Medicina")

estudiante1.atributoss()
estudiante1.clase("Programación")
estudiante2.atributoss()
estudiante2.clase("Morfofisiología")