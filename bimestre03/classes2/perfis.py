from crud import CRUD
import json

class Perfil:
    def __init__(self, id, nome, desc, beneficio):
        self.id = id
        self.nome = nome
        self.desc = desc
        self.beneficio = beneficio
    def __str__(self):
        return f"{self.nome} - {self.desc} - {self.beneficio}"

class Perfis(CRUD):
    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            c.nome = obj.nome
            c.desc = obj.desc
            c.beneficio = obj.beneficio
            
        cls.salvar()
    
    @classmethod
    def salvar(cls):
        with open("perfis.json", mode="w") as arquivo:   # w - write
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("perfis.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Perfil(obj["id"], obj["nome"], obj["desc"], obj["beneficio"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass
