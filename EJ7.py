"""7. Escribe un programa que recorra una cadena de 
texto y cuente cuántas veces aparece la letra 'a' en la cadena."""

texto = input("Ingrese una cadena de texto: ")

contador = 0

for letra in texto:
    if letra == 'a':
        contador += 1

print(f"La letra 'a' aparece {contador} veces.")
