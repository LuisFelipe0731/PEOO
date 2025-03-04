import json
from Models.crud import CRUD

class Usuario:
    def __init__(self,id, nome, email, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha

     
        

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email}"
    #to_json
    def to_json(self):
        dic = {}
        dic['id'] = self.id  
        dic['nome'] = self.nome
        dic['email'] = self.email
        dic['senha'] = self.senha
        return dic


class Usuarios(CRUD):
    def atualizar(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            c.nome = obj.nome
            c.email = obj.email
            c.senha = obj.senha  
        cls.salvar()
 
    @classmethod
    def salvar(cls):
        try:
            with open("Usuarios.json", mode="w") as arquivo:   # w - write
                json.dump(cls.objetos, arquivo, default = Usuario.to_json)
        except FileNotFoundError:
            pass

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Usuarios.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Usuario(obj['id'], obj['nome'], obj['email'], obj['senha'])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass
    
    