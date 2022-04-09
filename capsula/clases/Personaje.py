class Personaje:
    
    def __init__(self):
        self.__nombre = None 
        self.__edad = None

    @property 
    def nombre(self):
        return self.__nombre 
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property 
    def edad(self):
        return self.__edad 

    @edad.setter
    def edad(self, edad):
        if(edad<0):
            print("no se acepto la edad")
        else:
            self.__edad = edad
    