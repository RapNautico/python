#Construir un programa que reciba el tamaño de una lista
#y la llene con números entregados por el usuario

numeros = []

tamaño = int(input("Ingrese el tamaño de la lista: "))

for i in range(tamaño):
    numero = int(input("Ingrese un numero: "))
    numeros.append(numero)
print(numeros)
