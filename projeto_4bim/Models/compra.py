import json
from Models.crud import CRUD

class Compra:
    def __init__(self, id):
        self.__id = 0
        self.__id_user = 0
        self.__id_exemp = 0

        self.set_id(id)
        
    #set e get
    def set_id(self,id):
        if id != 0:
            self.__id = id
        else:
            raise ValueError("Valor invalido")

    def get_id(self): return self.__id

    def __str__(self):
        return f"{self.__id} - R$ {self.__valor}"

    def to_json(self):
        dic = {}
        dic["id"] = self.__id  
        dic["usuario"] = self.__id_user
        dic["exemplar"] = self.__id_exemp
        return dic



class Compras(CRUD):
    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
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
                    c = Compra(obj["id"])
                    c.__id_user = obj["usuario"]
                    c.__id_exemp = obj["exemplar"]
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass