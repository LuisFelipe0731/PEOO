from datetime import datetime
import json
#classes -->

#Professor
class Professsor:
    def __init__(self, id, nome, diretoria, materia):
        self.id = id
        self.nome = nome
        self.diretoria = diretoria
        self.materia = materia
    
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.diretoria} - {self.materia}"

#Curso
class Curso:
    def __init__(self, id, nome, diretoria, tempo_de_conclusao):
        self.id = id
        self.nome = nome
        self.diretoria = diretoria
        self.t = tempo_de_conclusao
    
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.diretoria} - {self.t.strftime('%d/%m/%Y %H:%M')}"
    
    def to_json(self):
        dic = {}
        
        dic["id"] = self.id
        dic["nome"] = self.nome
        dic["diretoria"] = self.diretoria
        dic["tempo de conclusâo"] = self.t.strftime('%d/%m/%Y %H:%M')
        return dic

#Diretoria
class Diretoria:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.id_professor = 0
        self.id_curso = 0
    
    def __str__(self):
        return f"{self.id} - {self.nome}"
    
#Cruds -->

#professores
class Professores:
    professores = []
    
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0                     
        for c in cls.professores:     
            if c.id > m: m = c.id   
            obj.id = m + 1  
            cls.professores.append(obj)
            cls.salvar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.professores
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for c in cls.professores:
            if c.id == id: return c
        return None 
    
    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            c.nome = obj.nome          
            c.diretoria = obj.diretoria
            c.materia = obj.materia     
            cls.salvar()   
    
    @classmethod
    def excluir(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None: 
        cls.professores.remove(c)
        cls.salvar()   
    
    @classmethod
    def salvar(cls):  
        with open("professores.json", mode = "w") as arquivo:   
            json.dump(cls.professores, arquivo, default = vars) 
    
    @classmethod
    def abrir(cls):
        cls.professores = []
        try: 
            with open("professores.json", mode = "r") as arquivo:  
                texto = json.load(arquivo)
                for obj in texto:
                    c = Professsor(obj[)             
                cls.professores.append(c)
        except FileNotFoundError:
            pass