# Clase 2020/9/4 - Prácticas con ciclos while, for y listas.

# ----- ADIVINANDO EL NÚMERO DEL DADO ----- #
import random

Dado = random.randint (1,6)
Falla = 0

NumberQ = "Ingrese un número del dado para adivinar: "
Numero = int (input(NumberQ))

Falso = "No adivinaste el número del dado."
Verdadero = "Felicitaciones! Has adivinado el número que ha salido en el dado."
Resultado = f"El número obtenido del dado fue {Dado}."
Fallas = "Te equivocaste {} veces."
Bye = "Gracias por jugar!"

while (Numero != Dado):
    Falla += 1
    print(Falso)
    print("")
    Numero = int(input(NumberQ))
    print("")

print(Verdadero)
print("")
print (Resultado)
print("")
print (Fallas.format(Falla))
print("")
print(Bye)

# ----- COMIDAS FAVORITAS ----- #

FoodList = []

FoodQ = "Ingrese su comida favorita: "
MoreFoodQ = ("""Necesita ingresar otra comida?""
    Si - Agregar otra comida.
    No - Finalizar listado
                    
    Respuesta: """)

Go = "Si"

while (Go == "Si"):
    Food = input (FoodQ)
    FoodList.append (Food)
    print ("")
    Go = input (MoreFoodQ)

Size = len (FoodList)
print ("")
print (f"Su lista tiene {Size} comidas registradas:")
print("")

for i in range (Size):
    print (FoodList [i])

print ("")
print (f"Su tercera comida favorita es {FoodList [2]}.")