# Clase 2020/8/12 - Condicionales
Nombre = input ("Por favor ingrese su nombre:")
print ("Hola", Nombre, "Bienvenido a este código!")
Edad = int (input("Por favor ingrese su edad:"))
Estatura = float (input("Por favor ingrese su estatura:"))

print (Nombre)
print (Edad)
print (Estatura)

print (type(Nombre))
print (type(Edad))
print (type(Estatura))

if (Edad >= 18) :
    print ("Usted es mayor de edad")
    print ("Ya eres adulto!")

if (Estatura >= 1.70) :
    print ("Eres muy alto!")

print ("Chao que te vaya super bien")