#Leer 20 números enteros y guardar en una lista,
#después permitir que el usuario busque un número y 
#si este se encuentra en la lista indicar 
#con un mensaje que el resultado es exitoso
numeros = []

for i in range(0, 5):
    numero = int(input("escriba el numero que va a buscar: "))
    numeros.append(numero)

buscar = int(input("Elija el numero a buscar: "))

if(buscar in numeros):
    print("si esta en la lista")
else:
    print("no hay nada")

