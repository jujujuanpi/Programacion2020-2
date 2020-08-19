# Taller 2020/08/19. Cálculo de Índice de Masa Corporal

print ("Bienvenido al calculador de IMC. Por favor, ingrese los siguientes datos.")

Nombre = input("Ingrese su nombre: ")
Peso = float(input("Ingresar su peso en kilogramos: "))
Estatura = float(input("Ingresar su estatura: "))
IMC = Peso / Estatura**2

print (Nombre, Peso, Estatura)

if (IMC < 18.5):
    print ("El paciente {Nombre} se encuentra en un estado de infrapeso.")
elif (IMC >= 18.5 and IMC < 24.9):
    print ("El panciente {Nombre} se encuentra con un peso normal.")
elif (IMC >= 25 and IMC < 30):
    print ("El panciente {Nombre} se encuentra con sobrepeso.")
elif (IMC >= 30 and IMC < 35):
    print ("El panciente {Nombre} presenta un estado de obesidad.")
else:
    print ("El paciente {Nombre} presenta obesidad mórbida.")

print ("Gracias por participar.")