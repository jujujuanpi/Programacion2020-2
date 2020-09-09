# Taller de Repaso de Todo - Tratado de Temperaturas de Neonatos

# Entradas
Temperatura_Corporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]

# Preguntas
Menu = """
Por favor seleccione una opción.

1. Conversión de Temperaturas
2. Estado de Salud
3. Visualización de Temperatura Máxima y Mínima
4. Salir del Programa

Respuesta: """

Conversion = """
Por favor seleccione una opción.

K. Conversión a Kelvin
F. Conversión a Fahrenheit
C. Conversión a Celcius

Respuesta: """

# Mensajes
Error = "No ha escogido una de las opciones del menú. Por favor intente de nuevo."
Op = "Ha escogido la opción: {}"
Bye = "Gracias por usar el programa."
Hi = "Bienvenido al programa."
Cel = "No es necesario hacer una conversión."
Big = "La temperatura máxima del listado es de {}"
Small = "La temperatura mínima del listado es de {}"
Frec = "La frecuencia en la que se tomaron las temperaturas es de {}"

# Inicio del código
Option = int (input(Menu))
print ("")

# Cálculos
ListaK = []
ListaF = []
ListaC = Temperatura_Corporal
ListaSalud = []

# --- De C a K --- #
for Elemento in ListaC:
    Kelvin = Elemento + 273.15
    ListaK.append(Kelvin)
# --- De C a F --- #
for Elemento in ListaC:
    Fahrenheit = (Elemento*1.8) + 32
    ListaF.append(Fahrenheit)

# --- Detección de Estado de Salud --- #
for Elemento in ListaC:
    Estado = ""
    if (Elemento < 36):
        Estado = "Hipotermia"
    elif (Elemento >= 36 and Elemento < 37.6):
        Estado = "Saludable"
    else:
        Estado = "Fiebre"
    ListaSalud.append(Estado)

# --- Cálculo de máximo y mínimo --- #
Mayor = max (ListaC) # max para calcular el valor mayor de una lista
Menor = min (ListaC) # min para calcular el valor menor de una lista
Frecuencia = round(len (ListaC)/24,3) # round para redondeo de decimales

# Respuesta a menú
while (Option != 4):
    if (Option == 1):
        print (Op.format(1))
        # Pregunta de Conversión
        OptionT = input (Conversion) # Se pueden crear variables únicas para un if
        print ("")
        if (OptionT == "K"):
            print (ListaK)
        elif (OptionT == "F"):
            print (ListaF)
        elif (OptionT == "C"):
            print (Cel)
            print(ListaC)
        else:
            print (Error)
    elif (Option == 2):
        print (Op.format(2))
        # Lista de Estados de Salud
        print ("")
        print (ListaSalud)
    elif (Option ==3):
        print (Op.format(3))
        # Resultado de máximo y mínimo
        print ("")
        print (Big.format(Mayor))
        print (Small.format(Menor))
        print (Frec.format(Frecuencia))
    else:
        print (Error)
    # Entrada de opción
    Option = int (input(Menu))

#Salida del programa
print (Bye)