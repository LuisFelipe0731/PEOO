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

        except:
            id = 0

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


class Livros(CRUD):
    @classmethod
    def atualizar(cls, obj):
        pass
    @classmethod
    def salvar(cls):
        pass
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("horarios.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                c = Horario(obj["id"], datetime.strptime(obj["data"], "%d/%m/%Y %H:%M"))
                c.__confirmado = obj["confirmado"]
                c.__id_cliente = obj["id_cliente"]
                c.__id_servico = obj["id_servico"]
                cls.objetos.append(c)
        except FileNotFoundError:
            pass