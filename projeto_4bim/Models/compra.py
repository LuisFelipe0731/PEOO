import json
from Models.crud import CRUD

class Compra:
    def __init__(self, id, valor):
        self.__id = 0
        self.__valor = 0
        self.__id_user = 0
        self.__id_exemp = 0

        self.set_id(id)
        self.set_valor(valor)
        
    #set e get
    def set_id(self,id):
        if id != 0:
            self.__id = id
        else:
            raise ValueError("Valor invalido")

    def set_valor(self,v):
        if v != 0:
            self.__valor = v
        else:
            raise ValueError("A compra precisa ter um valor")
    
    def get_id(self): return self.__id
    def get_valor(self): return self.__valor
    
    def __str__(self):
        return f"{self.__id} - R$ {self.__valor}"

    def to_json(self):
        dic = {}
        dic["id"] = self.__id  
        dic["valor"] = self.__valor
        dic["usuario"] = self.__id_user
        dic["exemplar"] = self.__id_exemp
        return dic



class Compras(CRUD):
    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            c.__valor = obj.__valor
            c.__id_user = obj.__id_user
            c.__id_exemo = obj.__id_exemp
        cls.salvar()
        
    
    @classmethod
    def salvar(cls):
        with open("Compras.json", mode="w") as arquivo:   # w - write
            json.dump(cls.objetos, arquivo, default = Compra.to_json)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Compras.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Compra(obj["id"],obj["valor"])
                    c.__id_user = obj["usuario"]
                    c.__id_exemp = obj["exemplar"]
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass