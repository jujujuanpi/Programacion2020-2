# Clase 2020/8/28 - Cliclos

# ----- NÚMERO SECRETO ----- #
# VARIABLES

#    PREGUNTAS
PreguntaNumero = ('Ingrese su número del 1 al 10: ')

#    MENSAJES
IfFalse = 'No adivinaste el número secreto.'
IfTrue = 'Felicitaciones! Has adivinado el número secreto.'
Bye = 'Gracias por jugar!'
Loss = 'Has perdido {} vida. Aún tienes {} vidas.'
IfLoss = 'Se ha acabado el juego.'

#    NÚMEROS
NumeroSecreto = 6
Numero = int(input(PreguntaNumero))
Vidas = 3

while(NumeroSecreto != Numero and Vidas >= 1):
    Vidas = Vidas -1
    print(IfFalse)
    print (Loss.format(3-Vidas , Vidas))
    if Vidas > 0:
        Numero = int(input(PreguntaNumero))

if Vidas >0:
    print(IfTrue)
else:
    print(IfLoss)

print(Bye)

# ----- LETRA SECRETA ----- #
# VARIABLES

#    PREGUNTAS
PreguntaLetra = ('Ingrese una vocal: ')

#    MENSAJES
IfFalse = 'No adivinaste la letra secreta.'
IfTrue = 'Felicitaciones! Has adivinado la letra secreta.'
Bye = 'Gracias por jugar!'

#    LETRAS
LetraSecreta = 'A'
Letra = input(PreguntaLetra).upper()

while(LetraSecreta != Letra):
    print(IfFalse)
    Letra = input(PreguntaLetra)

print(IfTrue)

print(Bye)
