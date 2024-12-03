from crud import CRUD

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
    super.__init__()