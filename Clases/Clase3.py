# Clase 2020/8/14 - Condicionales
#     NÚMEROS MAYORES Y MENORES

A = int (input("Ingrese el primer número entero: "))
B = int (input("Ingrese el segundo número entero: "))

print (A,B)

if (A == B):
    print ("Son números iguales.")
elif (A > B):
    print ("El número", A, "es mayor que el número", B, ".")
else:
    print (f"El número {B} es mayor que el número {A}.")

print ("Chao")


#     DADA UNA TEMPERATURA DETERMINAR SI EL PACIENTE ESTA SANO O NO
#       Temp mayor a 36, hipotermia; entre 36 y 37.5, normal; entre 37.5 y 38, alerta; mayor a 38, fiebre
#       Nombre y temp

Nombre = input ("Ingrese el nombre del paciente: ")
Temperatura = float (input("Ingrese la temperatura medida: "))

print (Nombre,Temperatura)

if (Temperatura < 36):
    print (f"El paciente {Nombre} sufre de hipotermia.")
elif (Temperatura >= 36 and Temperatura < 37.5):
    print (f"El paciente {Nombre} presenta una temperatura normal.")
elif (Temperatura >= 37.5 and Temperatura < 38):
    print (f"El paciente {Nombre} presenta una temperatura moderada. Estado de alerta.")
else:
    print (f"El paciente {Nombre} presenta fiebre.")

if (Temperatura < 36 or Temperatura >= 38):
    print ("Consulte con su médico para conocer sus opciones.")

print ("Gracias por venir a consulta!")