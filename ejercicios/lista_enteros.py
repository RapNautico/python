numeros = []

for i in range(0, 5):
    numero = int(input("escriba el numero que va a buscar: "))
    numeros.append(numero)

buscar = int(input("Elija el numero a buscar: "))

if(buscar in numeros):
    print("si esta en la lista")
else:
    print("no hay nada")

