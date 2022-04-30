from clases.Persona import Persona

class Cliente(Persona): 

    def __init__(self, saldo):
        self.__saldo = saldo
    
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
    

    