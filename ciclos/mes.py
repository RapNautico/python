#Ejemplo de estaciones

mes = input("Digita un mes del año: ").lower()

if(mes == "diciembre" or mes == "enero" or mes == "febrero" or mes == "marzo"):
    print(f"{mes} se encuentra en invierno")
elif(mes == "junio" or mes == "julio" or mes == "agosto"):
    print(f"{mes} se encuentra en verano")
elif(mes == "abril" or mes == "mayo"):
    print(f"{mes} se encuentra en primavera")
elif(mes == "septiembre" or mes == "octubre" or mes == "noviembre"):
    print(f"{mes} se encuentra en OTOÑO")
else:
    print("Lo que ingresaste no es un mes")
