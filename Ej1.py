"""1. Escribe un programa que identifique el color
de un objeto y muestre un mensaje según el color."""

Color = "Rojo"
aux = False

while aux == False :
 Pregunta = input("Que color es el lapiz ",  )
 if Pregunta == Color :
     print("Correcto")
     aux = True
 else :
     print("Incorrecto intenta de nuevo")