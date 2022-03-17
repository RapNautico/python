#Construir un programa que reciba el tamaño de una lista  y la llene con múltiplos de 7

multiplos = [1]

longitudLista = int(input("Ingrese el tamaño de la lista: "))

for i in range(longitudLista):
    multiplos.append((i+1) * 7)

print(multiplos)