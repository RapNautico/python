#Una clase es un molde
class Heroe:
    #Constructor de la clase
    # constructor = funcion especial
    # constructor = funcion que permite inicializar los atributos 
    def __init__(self, nombre,poder, estatura) -> None:
        #atributos = propiedades = datos
        #Variables del lenguaje que yo elija
        self.nombre = nombre
        self.poder = poder
        self.estatura = estatura
        self.clasificacion = None
        self.cantidadVida = None
        pass
    #metodos = acciones = ¿qué hace mi molde?
    #Funciones del lenguaje que yo elija
    def saludar(self):
        print(f"Hola {self.nombre}, tienes una estatura de {self.estatura}")

#Utilizando la clase = crear una instancia

#Un objeto es una variable especial
batman = Heroe("Bruce Wayne", "Invisible", 1.90)
#con el objeto accedo a un atributo
# batman.nombre = "Bruce Wayne"
print(batman.nombre)

#Con el objeto accedo a un metodo(funcion)
batman.saludar()