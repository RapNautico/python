#diccionario dentro de una lista
estudiantes = [
    {'nombre': 'juan', 'edad':20},
    {'nombre': 'camila', 'edad':24}
]

# print(estudiantes)

clases = [estudiantes]

for clase in clases:
    print(clase)

#lista dentro de un diccionario
print("--------------------------------")
estudiantes = []

for numeroEstudiantes in range(5):
    nuevoEstudiante = {'años': 20, 'nombre': 'Emanuel'}
    estudiantes.append(nuevoEstudiante)
#mostrar los primeros estudiantes
for estudiante in estudiantes[:5]:
    print(estudiante)
print("--------------------------------")

#ver la cantidad de estudiantes creados
print(f"se han creado {str(len(estudiantes))} estudiantes ")