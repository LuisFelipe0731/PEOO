import json
from crud import CRUD

class Exemplar:
    def __init__(self, id, edicao):
        self.__id = 0
        self.__ed = ""
        self.__id_livro = 0
    
    #set e get 
    
    def __str__(self):
        return f"{self.__id} - {self.__ed}"
    
    def to_json(self):

        

class Exemplares(CRUD):