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
        self.__id_genero = 0

        self.Set_valores(id, titulo, autor, data)
    
    #get e set
    def Set_valores(self,id, t, a, d):
        try:
            self.__id = id

        except id == 0:
            raise ValueError
            
    def Get_valores(self):
        return self.__id


    #str
    def __str__(self):
        return f"{self.__id} - {self.__titulo} - {self.__autor} - {self.__data_publicacao}"
    
    #to_json
    def to_json(self):
        dic = {}
        dic["id"] = self.__id  
        dic["titulo"] = self.__titulo
        dic["autor"] = self.__autor 
        dic["data"] = self.__data_publicacao.strftime("%d/%m/%Y %H:%M")
        dic["genero"] = self.__id_genero
        return dic

#crud
class Livros(CRUD):
    @classmethod
    def atualizar(cls, obj):
        pass
    
    @classmethod
    def salvar(cls):
        with open("livros.json", mode="w") as arquivo:   # w - write
            json.dump(cls.objetos, arquivo, default = Livro.to_json)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Livros.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Livro(obj["id"],obj["titulo"], obj["autor"], datetime.strptime(obj["data"], "%d/%m/%Y %H:%M"))
                    c.__id_genero = obj["genero"]
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass