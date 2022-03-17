#Convertir la tupla=(50,45,20,30,40,87) en una lista que solo contenga números > 40
print("---------MAYOR A 40-----------")
numeros  = (50, 45,20,30,40,87)

listaNumeros = []
for i in range(len(numeros)):
    if numeros[i]>40:
        listaNumeros.append(numeros[i])

print(listaNumeros)

#Convertir la tupla=(50,45,20,30,40,87) en una lista que solo contenga números  PARES
print("---------PARES-----------")
numeros = (50,45,20,30,40,87)

listaNumeros = []

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        listaNumeros.append(numeros[i])

print(listaNumeros)

#Convertir la tupla=(50,45,20,30,40,87) en una lista que solo contenga números  IMPARES
print("---------IMPARES-----------")
numeros = (50,45,20,30,40,87)

listaNumeros = []

for i in range(len(numeros)):
    if numeros[i] % 2:
        listaNumeros.append(numeros[i])

print(listaNumeros)