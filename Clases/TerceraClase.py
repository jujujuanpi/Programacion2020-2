# Clase 2020/8/14 - Condicionales
A = int (input("Ingrese el primer número entero: "))
B = int (input("Ingrese el segundo número entero: "))
print (A,B)

if (A == B):
    print("Son números iguales.")
elif (A > B):
    print("El número", A, "es mayor que el número", B, ".")
else:
    print(f"El número {B} es mayor que el número {A}.")

print("Chao")