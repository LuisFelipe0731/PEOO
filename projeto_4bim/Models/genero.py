import json
from Models.crud import CRUD

class Genero:
    def __init__(self,id, nome, descricao):
        self.__id = 0
        self.__nome = ""
        self.__desc = ""

        self.set_id(id)
        self.set_nome(nome)
        self.set_desc(descricao)
    
    #set e get
    def set_id(self,id):
        if id != 0:
            self.__id = id
        else:
            raise ValueError("Valor invalido")

    def set_nome(self,n):
        if n != "":
            self.__nome = n
        else:
            raise ValueError("O genero precisa de um nome")
    
    def set_desc(self,d):
        if d != "":
            self.__desc = d
        else:
            raise ValueError("O genero precisa de uma descrição")
        
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_desc(self): return self.__desc
  
        

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__desc}"
        
        
class Generos(CRUD):
    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            c.__nome = obj.__nome
            c.__desc = obj.__desc

        cls.salvar()
        
    
    @classmethod
    def salvar(cls):
        with open("Generos.json", mode="w") as arquivo:   # w - write
            json.dump(cls.objetos, arquivo, default = vars)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Generos.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Genero(obj["id"],obj["nome"], obj["desc"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass