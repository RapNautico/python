#Lista de datos
#Leer 8 ciudades colombianas, guardarlas en una lista y mostrar en orden inverso los datos ingresados
ciudades = ['Medellin', 'Cali', 'Bogota', 'Santa Marta', 'Cartagena']

#Esculcando en la lista
for ciudad in reversed(ciudades):
    print(ciudad)


#Arreglo
print("-----------SUMA--------------")
numeros=[1,2,3,4,5]
suma = 0

for numero in numeros:
    suma+=numero
    # suma+=1
    
print(suma)