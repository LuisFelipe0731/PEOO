from crud import CRUD
import json

class Cliente:
    def __init__(self, id, nome, email, fone, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
        self.senha = senha
        self.id_perfil = 0
    def __str__(self):
        return f"{self.nome} - {self.email} - {self.fone}"
    def to_json(self):
        dic = {}
        dic["id"] = self.id
        dic["nome"] = self.nome
        dic["email"] = self.email
        dic["fone"] = self.fone
        dic["senha"] = self.senha
        dic["id_perfil"] = self.id_perfil
        return dic    

class Clientes(CRUD):
    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:   # w - write
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"], obj["senha"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass