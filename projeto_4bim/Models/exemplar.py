import json
from crud import CRUD

class Exemplar:
    def __init__(self, id, edicao):
        self.__id = 0
        self.__ed = ""
        self.__id_livro = 0

        self.set_id(id)
        self.set_edicao(edicao)
    
    #set e get 
    def set_id(self,id):
        if id != 0:
            self.__id = id
        else:
            raise ValueError("Valor invalido")

    def set_edicao(self,e):
        if e != "":
            self.__ed = e
        else:
            raise ValueError("O exemplar precisa de uma edição")
    
    def get_id(self): return self.__id
    def get_edicao(self): return self.__ed


    def __str__(self):
        return f"{self.__id} - {self.__ed}"
    
    def to_json(self):
        dic = {}
        dic["id"] = self.__id  
        dic["edição"] = self.__ed
        dic["livro"] = self.__id_livro
        return dic

        

class Exemplares(CRUD):