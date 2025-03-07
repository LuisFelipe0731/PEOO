import json
from Models.crud import CRUD

class Exemplar:
    def __init__(self, id, edicao, valor):
        
        if id < 0: raise ValueError
        if edicao == "": raise ValueError
        if valor == 0: raise ValueError
        
        self.id = id
        self.ed = edicao
        self.valor = float(valor)
        self.id_livro = 0

    
    
    def __str__(self):
        return f"{self.id} - {self.ed} - {self.valor}"
    
    def to_json(self):
        dic = {}
        dic['id'] = self.id  
        dic['edição'] = self.ed
        dic['valor'] = self.valor
        dic['livro'] = self.id_livro
        return dic

class Exemplares(CRUD):
    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            c.ed = obj.ed
            c.valor = obj.valor
            c.id_livro = obj.id_livro
        cls.salvar()
        
    @classmethod
    def salvar(cls):
        with open("Exemplares.json", mode="w") as arquivo:   # w - write
            json.dump(cls.objetos, arquivo, default = Exemplar.to_json)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Exemplares.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Exemplar(obj['id'], obj['edição'], obj['valor'])
                    c.id_livro = obj['livro']
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass
    