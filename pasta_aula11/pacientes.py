import json
import datetime

#classe paciente
class Paciente:
    def __init__(self,id,nome,fone,nasc):
        self.__id = 0
        self.__nome = ""
        self.__fone = ""
        self.__nasc = ""
        self.set_id(id)
        self.set_nome(nome)
        self.set_fone(fone)
        self.set_nasc(nasc)

    def set_id(self,x):
        if x > 0: self.__id = x
        else: raise ValueError
    def set_nome(self,n):
            if n != "": self.__nome = n
            else: raise ValueError
    def set_fone(self,f):
            if f != "": self.__fone = f
            else: raise ValueError
    def set_nasc(self,data):
            if data != "": self.__data = data
            else: raise ValueError
    
    
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.fone} - {self.nasc}"
    
class Pacientes:

class UI:
        
        