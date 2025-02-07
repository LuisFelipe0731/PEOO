import json
from datetime import datetime
from crud import CRUD

#Livro
class Livro():
    def __init__(self,id, titulo, autor, data,):
        self.__id = 0
        self.__titulo = ""
        self.__autor = ""
        self.__data_publicacao = ""
        self._id_genero = 0

        self.Set_valores(id, titulo, autor, data)
    
    #get e set
    def Set_valores(id, t, a, d):
        try:
            self.__id = id

        except:
            id = 0

    #str
    def __str__(self):
        return f"{self.__id} - {self.__titulo} - {self.__autor} - {self.__data_publicacao}"
    
    #to_json

class Livros(CRUD):
    @classmethod
    def atualizar(cls, obj):
        pass
    @classmethod
    def abrir(cls):
        pass
    
    @classmethod
    def salvar(cls):
        pass