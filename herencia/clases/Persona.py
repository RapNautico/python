class Persona:

    def _init_(self, nombre, telefono, edad, direccion, correo):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__edad = edad
        self.__direccion = direccion
        self.__correo = correo

    def _str_(self):
        return f"{self.__nombre} - {self.__telefono} - {self.__edad} - {self.__direccion} - {self.__correo}"

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def telefono(self):
        return self.__telefono
    
    @telefono.setter
    def telefono(self, telefono):
        self.__telefono = telefono
    
    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad
    
    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, correo):
        self.__correo = correo
    
    def mostrar_datos(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Telefono: {self.__telefono}")
        print(f"Edad: {self.__edad}")
        print(f"Direccion: {self.__direccion}")
        print(f"Correo: {self.__correo}")

Persona.mostrar_datos("Juan", 123456789, 30, "Calle falsa 123", "test@test.com")