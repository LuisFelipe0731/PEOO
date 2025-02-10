import json
from datetime import datetime
from crud import CRUD

#Livro
class Livro:
    def __init__(self, id, titulo, autor, data):
        self.__id = 0
        self.__titulo = ""
        self.__autor = ""
        self.__data_publicacao = ""
        self.__id_genero = 0
        
        #sets
        self.set_id(id)
        self.set_titulo(titulo)
        self.set_autor(autor)
        self.set_data(data)
    #--get e set--
    
    #set
    def set_id(self,id):
        if id != 0:
            self.__id = id
        else:
            raise ValueError("Valor invalido")

    def set_titulo(self,t):
        if t != "":
            self.__titulo = t
        else:
            raise ValueError("O livro precisa de um titulo")
    
    def set_autor(self,a):
        if a != "":
            self.__autor = a
        else:
            raise ValueError("O livro precisa de um autor")
        
    def set_data(self,d):
        if d != '':
            self.__data_publicacao = d
        else:
            raise ValueError("É preciso ter uma data")
        
    #get
    def get_id(self): return self.__id
    def get_titulo(self): return self.__titulo
    def get_autor(self): return self.__autor
    def get_data(self): return self.__data_publicacao
   
        


    #str
    def __str__(self):
        return f"{self.__id} - {self.__titulo} - {self.__autor} - {self.__data_publicacao}"
    
    #to_json
    def to_json(self):
        dic = {}
        dic["id"] = self.__id  
        dic["titulo"] = self.__titulo
        dic["autor"] = self.__autor 
        dic["data"] = self.__data_publicacao.strftime("%d/%m/%Y")
        dic["genero"] = self.__id_genero
        return dic

#crud
class Livros(CRUD):
    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            c.__titulo = obj.__titulo
            c.__autor = obj.__autor
            c.__data_publicacao = obj.__data_publicacao
            c.__senha = obj.__senha
            c.__id_genero = obj.__id_genero
        cls.salvar()
        
    
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
                    c = Livro(obj["id"],obj["titulo"], obj["autor"], datetime.strptime(obj["data"], "%d/%m/%Y"))
                    c.__id_genero = obj["genero"]
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass