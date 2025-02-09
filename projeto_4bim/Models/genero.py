import json
from crud import CRUD

class Genero:
    def __init__(self,id, nome, descricao):
        self.__id = 0
        self.__nome = ""
        self.__desc = ""
    #set e get
        

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__desc}"
        
        
class Generos(CRUD):