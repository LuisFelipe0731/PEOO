import json
from datetime import datetime


#cliente
class Cliente:
    def __init__(self, id, nome, email, fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
    
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"
    

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
    def listar(cls):
        cls.abrir()
        return cls.objetos
    
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
        cls.salvar()   
    
    @classmethod
    def excluir(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None: 
            cls.objetos.remove(c)
            cls.salvar()   
    
    @classmethod
    def salvar(cls):  
        with open("clientes.json", mode = "w") as arquivo:   # write
            json.dump(cls.objetos, arquivo, default = vars) 
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try: 
            with open("clientes.json", mode = "r") as arquivo:   # read
                texto = json.load(arquivo)
                for obj in texto:
                    c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])            
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass
    
#horario
class Horario:
    def __init__(self,id,data):
        self.id = id
        self.data = data
        self.comfirmado = False

    def __str__(self):
        return f"{self.id} - {self.data.strftime('%d/%m %H:%M')}"

class Horarios:
    horarios = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        n = 0                     
        for h in cls.horarios:     
            if h.id > n:
                n = h.id   
        obj.id = n + 1  
        cls.horarios.append(obj)
        cls.salvar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.horarios
   
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for h in cls.horarios:
            if h.id == id: return h
        return None

    @classmethod
    def atualizar(cls, obj):
        h = cls.listar_id(obj.id)
        if h != None:
            h.data = obj.data
            h.comfirmado = obj.comfirmado
          
        cls.salvar()
    
    @classmethod
    def excluir(cls, obj):
        h = cls.listar_id(obj.id)
        if h != None: 
            cls.horarios.remove(h)
        cls.salvar()
        
    @classmethod
    def salvar(cls):  
        with open("Horarios.json", mode = "w") as arquivo2:  
            json.dump(cls.horarios, arquivo2, default = vars) 
    
    @classmethod
    def abrir(cls):
        cls.horarios = []
        try: 
            with open("Horarios.json", mode = "r") as arquivo2:   
                texto1 = json.load(arquivo2)
                for obj in texto1:
                    h = Horario(obj["id"], obj["data"], obj["comfirmado"])                    
                    cls.horarios.append(h)
        except FileNotFoundError:
            pass
    

#serviço
class Servico:
    def __init__(self,id,descricao,valor,tempo):
        self.id = id
        self.desc = descricao
        self.valor = valor
        self.t = tempo
    def __str__(self):
        return f"{self.id} - {self.desc} - {self.valor} - {self.t.strftime('%H:%M')}"
       
class Servicos:
    serv = []
   
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        x = 0                     
        for s in cls.serv:     
            if s.id > x:
                x = s.id   
        obj.id = x + 1  
        cls.serv.append(obj)
        cls.salvar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.serv
   
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for s in cls.serv:
            if s.id == id: return s
        return None

    @classmethod
    def atualizar(cls, obj):
        s = cls.listar_id(obj.id)
        if s != None:
            s.descricao = obj.descricao
            s.valor = obj.valor
            s.tempo = obj.tempo
          
        cls.salvar()
    
    @classmethod
    def excluir(cls, obj):
        s = cls.listar_id(obj.id)
        if s != None: 
            cls.serv.remove(s)
        cls.salvar()
        
    @classmethod
    def salvar(cls):  
            with open("Serviços.json", mode = "w") as arquivo3:  
                json.dump(cls.serv, arquivo3, default = vars) 
    
    @classmethod
    def abrir(cls):
        cls.serv = []
        try: 
            with open("Serviços.json", mode = "r") as arquivo3:   
                texto2 = json.load(arquivo3)
                for obj in texto2:
                    s = Servico(obj["id"], obj["descricao"], obj["valor"], obj["tempo"])                    
                    cls.serv.append(s)
        except FileNotFoundError:
            pass