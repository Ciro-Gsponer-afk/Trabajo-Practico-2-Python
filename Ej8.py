"""8. Integrador:
Escribe un programa que permita a un usuario crear
una lista de nombres. El programa continuará pidiendo
nombres hasta que el usuario ingrese "fin". Luego, 
el programa mostrará la lista de nombres en orden alfabético,
indicará cuántos nombres empiezan con la letra 'A' o 'E', 
y mostrará si un nombre específico está en la lista."""
 
cont = 0
Nombre = input(f"Ingrese el Nombre N° {cont} : " )
lista = []

while True :
    if Nombre.lower() != "fin" :
     lista.append(Nombre)
     print(lista)
     cont +=1
     Nombre = input(f"Ingrese el Nombre N° {cont} : " )
    else :
     break

lista.sort()

print("\nLista ordenada:")
for na in lista:
    print(na)
contador_ae = 0
for na in lista:
    if na.lower().startswith("a") or na.lower().startswith("e"):
        contador_ae += 1

print(f"\nCantidad de nombres que empiezan con A o E: {contador_ae}")

buscar = input("\nIngrese un nombre para buscar: ")

if buscar in lista:
    print("El nombre SI está en la lista")
else:
    print("El nombre NO está en la lista")