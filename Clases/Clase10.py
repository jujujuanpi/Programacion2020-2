# Clase 2020/9/23 - Clases y Objetos

class TortasRedondas:
    def __init__ (self,saborIngresado):
        # Definición de atributos
        self.forma = "Redonda"
        self.sabor = saborIngresado
        # Acción al crear el objeto
        print ("Se ha ingresado una torta nueva")
    def atributos (self):
        print (f"Es una torta {self.forma} y tiene un sabor de {self.sabor}")

# Adición de tortas
Torta1 = TortasRedondas ("Chocolate")
Torta2 = TortasRedondas ("Vainilla")

# Mostrar en pantalla los atributos
print (Torta1.sabor)
print (Torta2.sabor)
print (Torta1.forma)
print (Torta2.forma)

Torta1.atributos()
Torta2.atributos()