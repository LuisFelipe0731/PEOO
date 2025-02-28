import json
from Models.crud import CRUD

class Exemplar:
    def __init__(self, id, edicao, valor):
        self.__id = 0
        self.__ed = ""
        self.__valor = 0
        self.__id_livro = 0

        self.set_id(id)
        self.set_edicao(edicao)
        self.set_valor(valor)
    
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
    
    def set_valor(self,s):
        if s <= 0:
            self.__valor = s
        else:
            raise ValueError("O valor precisa ser maior que 0")
    
    def get_id(self): return self.__id
    def get_edicao(self): return self.__ed
    def get_valor(self): return self.__valor


    def __str__(self):
        return f"{self.__id} - {self.__ed} - {self.__valor}"
    
    def to_json(self):
        dic = {}
        dic["id"] = self.__id  
        dic["edição"] = self.__ed
        dic["valor"] = self.__valor
        dic["livro"] = self.__id_livro
        return dic

class Exemplares(CRUD):
    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            c.__ed = obj.__ed
            c.__valor = obj.__valor
            c.__id_livro = obj.__id_livro
        cls.salvar()
        
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Exemplares.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Exemplar(obj["id"],obj["edição"],obj["valor"])
                    c.__id_livro = obj["livro"]
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("Exemplares.json", mode="w") as arquivo:   # w - write
            json.dump(cls.objetos, arquivo, default = Exemplar.to_json)
    