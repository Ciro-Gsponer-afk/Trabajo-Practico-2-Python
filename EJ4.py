import random

"""3. Escribe un programa que muestra la primer,
última u otra letra de una cadena de caracteres,
inclusive una rebanada."""



def Palabras():
    Palabra = input("Ingrese una palabra: ")
    print("Primera letra:", Palabra[0])
    print("Última letra:", Palabra[-1])
    

    medio = len(Palabra) // 2
    print("Letra del medio:", Palabra[medio])
    
    inicio = random.randint(0, len(Palabra) - 1)
    fin = random.randint(inicio + 1, len(Palabra))
    
    print("Rebanada aleatoria:", Palabra[inicio:fin])
    print(f"(Desde posición {inicio} hasta {fin})")

Palabras()