# Clase 2020/9/2 - Listas

#   ----- CREACIÓN DE LISTAS ----- #
NameList = []
NameList = ['Melany' , 'Karla' , 'Laura Paredes' , 'Laura Montoya' , 'Juan Pablo' , 'Mario' , 'Valeria' , 'Santiago']
AgeList = [20,18,18,18,21,20,18,18]

print (NameList)
print ("")
print (NameList [2])
print ("")
print (NameList [-1])
print ("")

NameList.append ('Daniel') #Agregar valor a la lista
print (NameList [-1])
print (NameList)

print ("")

NameList.pop(-1) #Borrar una posición de la lista
print (NameList)

NameList.append ("Daniel")
AgeList.append (27)

print ("")

Size = len (NameList) #Cálculo de tamaño de la lista
print (Size)

print ("")

for i in range (Size): #Para hacer un conteo de la lista tomando en cuenta la posición.
    print (f"Hola! Soy {NameList [i]} y estoy feliz programando.")

print ("")

for Nombre in NameList: #Para hacer un conteo de la lista más eficiente
    print (f"Hola! Soy {Nombre} y estoy feliz programando.")

print ("")

for i in range (Size):
    print (f"Nombre: {NameList [i]} y edad: {AgeList [i]}")

HobbyList = []

Go = "Si"

while (Go == "Si"):
    Hobby = input ("Ingrese su hobby favorito: ")
    HobbyList.append (Hobby)
    print ("")
    Go = input ("""Necesita ingresar otro hobby?""
                    Si - Agregar otro hobby.
                    No - Finalizar listado
                    
                    Respuesta:""")

print ("")
print(HobbyList)