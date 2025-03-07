import json
from datetime import datetime
from Models.crud import CRUD

#Livro
class Livro:
    def __init__(self, id, titulo, autor, data, genero):
        
        if id < 0: raise ValueError
        if titulo == "": raise ValueError
        if autor == "": raise ValueError
        if data == "": raise ValueError
        if genero == "": raise ValueError

        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.data_publicacao = data
        self.id_genero = genero
        
        
    #str
    def __str__(self):
        return f"{self.id} - {self.titulo} - {self.autor} - {self.data_publicacao} - {self.id_genero}"
    
    #to_json
    def to_json(self):
        dic = {}
        dic["id"] = self.id  
        dic["titulo"] = self.titulo
        dic["autor"] = self.autor 
        dic["data"] = self.data_publicacao.strftime('%d/%m/%Y')
        dic["genero"] = self.id_genero
        return dic

#crud
class Livros(CRUD):
    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            c.titulo = obj.titulo
            c.autor = obj.autor
            c.data_publicacao = obj.data_publicacao
            c.id_genero = obj.id_genero
        cls.salvar()
        

    @classmethod
    def salvar(cls):
        with open("livros.json", mode="w") as arquivo:   # w - write
            json.dump(cls.objetos, arquivo, default = Livro.to_json)
        
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("livros.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Livro(obj["id"],obj["titulo"], obj["autor"], datetime.strptime(obj["data"], "%d/%m/%Y"),obj["genero"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass
    