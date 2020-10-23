# Clase 2020/10/23 - GRÁFICOS DE TORTA

import matplotlib.pyplot as plt
lenguajes = ['Java','Python','C#','JavaScript','Dart']
sizes = [10,20,12,18,40]
explodeList = [0, 0.12, 0, 0, 0.12]
plt.title('Población de Desarrolladores')
plt.pie(sizes, labels=lenguajes)
plt.savefig('Desarrolladores.png')
plt.show()

lenguajes = ['Java','Python','C#','JavaScript','Dart']
sizes = [10,20,12,18,40]
explodeList = [0, 0.12, 0, 0, 0.12]
plt.title('Población de Desarrolladores')
plt.pie(sizes, labels=lenguajes, shadow=True, startangle=45)
plt.savefig('Desarrolladores.png')
plt.show()

lenguajes = ['Java','Python','C#','JavaScript','Dart']
sizes = [10,20,12,18,40]
explodeList = [0, 0.12, 0, 0, 0.12]
plt.title('Población de Desarrolladores')
plt.pie(sizes, labels=lenguajes, explode=explodeList)
plt.savefig('Desarrolladores.png')
plt.show()

preguntaObjetos = 'Ingrese cuantos elementos caben en la caja : '
preguntaIngresarObjeto = 'Ingrese nombre objeto '
preguntaIngresarObjetoOcupacion = 'Ingrese %ocupación del objeto '
elementos = []
ocupaciones = []
cantidad = int (input(preguntaObjetos))

for i in range(cantidad):
  elemento = input(preguntaIngresarObjeto)
  elementos.append(elemento)
  ocupacion = int (input(preguntaIngresarObjetoOcupacion))
  ocupaciones.append(ocupacion)

plt.title('Elementos en la caja vs ocupacion')
plt.pie(ocupaciones, labels= elementos, shadow=True, startangle=45)
plt.savefig ('cajaelementos.png')
plt.show()