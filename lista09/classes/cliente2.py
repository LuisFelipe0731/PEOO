import json
from datetime import datetime


# Cliente
class Cliente:
    def __init__(self, id, nome, email, fone, data):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
        self.data = data
        self.senha = 0
    def __str__(self):
        return f"{self.nome} - {self.email} - {self.fone} - {self.data}"
    
    def to_json(self):
        dic = {}
        dic["id"] = self.id
        dic["nome"] = self.nome
        dic["email"] = self.email
        dic["email"] = self.fone
        dic["data"] = self.data.strftime("%d/%m/%Y")
        dic["senha"] = self.senha
        return dic 


# Clientes
class Clientes:
    objetos = []   

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        for c in cls.objetos:
            if c.id > m: m = c.id
        obj.id = m + 1
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for c in cls.objetos:
            if c.id == id: return c
        return None  
    
    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            c.nome = obj.nome
            c.email = obj.email
            c.fone = obj.fone
            c.data = obj.data
        cls.salvar()

    @classmethod
    def excluir(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            cls.objetos.remove(c)
        cls.salvar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        cls.objetos.sort(key=lambda cliente: cliente.nome)
        return cls.objetos

    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:   # w - write
            json.dump(cls.objetos, arquivo, default = Cliente.to_json)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"], datetime.strptime(obj["data"], "%d/%m/%Y"))

                    cls.objetos.append(c)
        except FileNotFoundError:
            pass