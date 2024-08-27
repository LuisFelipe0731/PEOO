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
    
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.fone} - {self.nasc}"
    
class Pacientes:

class UI:
        
        