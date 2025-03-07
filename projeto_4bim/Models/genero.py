import json
from Models.crud import CRUD

class Genero:
    def __init__(self,id, nome, descricao):
        
        if id < 0: raise ValueError
        if nome == "": raise ValueError
        if descricao == "": raise ValueError
    
        self.id = id
        self.nome = nome
        self.desc = descricao
     
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.desc}"
        
class Generos(CRUD):
    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            c.nome = obj.nome
            c.desc = obj.desc
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
                    c = Genero(obj['id'], obj['nome'], obj['desc'])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass
    
