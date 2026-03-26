"""6. Escribe un programa que recorra una lista
de números y muestre si cada número es par o impar."""

Lista = [12,32,50,3,41,26,72,45,87,67,98,45,83,236]

for Num in Lista :
    if Num % 2 == 0 :
        print(f"El numero {Num} es par ")
    else :
     print(f"El Numero {Num} es impar ")
        