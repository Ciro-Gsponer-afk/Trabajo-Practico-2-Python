"""2.1. Escribe un programa que solicita al usuario
que ingrese números enteros positivos y muestre
la suma de esos números. La entrada de números
continuará hasta que el usuario ingrese un 
número negativo, momento en el que el programa 
mostrará la suma total."""


Total = 0
while True :
    Numeros = int(input("Ingrese un valor : ", ))
    
    if Numeros > 0 :
        Total +=   int(Numeros)
    else:
        break
print(Total)