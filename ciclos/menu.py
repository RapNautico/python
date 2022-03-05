import math

print("Empanadas el machetico")
print("**********************************************")
print("0. Salir")
print("1. Calcular la raiz cuadrada de un #")
print("2. Calcular la potencia 2 de un #")
print("**********************************************")

opcion = 1

while(opcion != 0):
    opcion = int(input("Digita una opcion: "))
    #pregunte por la opcion
    if(opcion == 0):
        break
    elif(opcion == 1):
        numero = int(input("Digita un numero: "))
        raiz = math.isqrt(numero)
        print(f"la raiz de {numero} es {raiz}: ")
    elif(opcion == 2):
        numero = int(input("Digita un numero: "))
        potencia = math.pow(numero, 2)
        print(f"la potencia de {numero} elevado es igaul a {potencia}")
    else:
        print("El numero no es valido")
        # break