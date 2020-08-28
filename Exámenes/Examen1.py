# Examen 2020/08/21. Medidor de Temperatura para Pasajeros Aéreos

print ("Bienvenido al aeropuerto. Por favor, ingrese los siguientes datos.")

Nombre = input("Ingrese su nombre: ")
Pais = input("Ingrese el país del que viaja: ")
Temperatura = float(input("Ingresar la temperatura corporal medida: "))

print (Nombre, Pais, Temperatura)


if (Temperatura < 36):
    print (f"El pasajero {Nombre} se encuentra en un estado de hipotermia.")
elif (Temperatura >= 36 and Temperatura < 38.5):
    print (f"El pasajero {Nombre} presenta un estado saludable.")
elif (Temperatura >= 38.5 and Temperatura < 40):
    print (f"El pasajero {Nombre} se encuentra en un estado de alerta.")
else:
    print (f"El pasajero {Nombre} se encuentra en un estado de peligro.")

if (Pais == 'Italia' or Pais == 'China' or Pais == 'Iran'):
    print (f"El pasajero se encuentra en estado de observación por su país de origen. Bienvenido a Colombia.")
else:
    print (f"El pasajero proviene de {Pais}. Bienvenido a Colombia.")


print ("Gracias por participar en la evaluación. Cuídese del COVID-19.")