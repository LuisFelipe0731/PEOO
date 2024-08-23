import json
import datetime
# Clientes, serviços e horarios

class Cliente:
    def __init__(self, nome, id, fone, email):
        self.id = id
        self.nome = nome
        self.fone = fone
        self.email = email   
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.fone} - {self.email}"
        

class Horario:
    def __init__(self,id,data,comfirmado):
        self.id = id
        self.data = data
        self.comfirmado = comfirmado
        id_cliente = Cliente.id
        id_servico = Serviço.id
    def __str__(self):
        return f"{self.id} - {self.data} - {self.comfirmado}"
        
class Serviço:
    def __init__(self,id,descricao,valor,tempo):
        self.id = id
        self.desc = descricao
        self.valor = valor
        self.t = tempo
    def __str__(self):
        return f"{self.id} - {self.desc} - {self.valor} - {self.t}"
       

#listas de Objetos
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
        with open("clientes.json", mode = "w") as arquivo:   
            json.dump(cls.objetos, arquivo, default = vars) 
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try: 
            with open("clientes.json", mode = "r") as arquivo:  
                texto = json.load(arquivo)
                for obj in texto:
                    c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])                    
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass

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
    
class Serviços:
    serv = []
   
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        x = 0                     
        for s in cls.horarios:     
            if s.id > x:
                x = s.id   
        obj.id = x + 1  
        cls.serv.append(obj)
        cls.salvar()
        
    @classmethod
    def salvar(cls):  
            with open("Serviços.json", mode = "w") as arquivo3:  
                json.dump(cls.horarios, arquivo3, default = vars) 
    
    @classmethod
    def abrir(cls):
            cls.horarios = []
            try: 
                with open("Serviços.json", mode = "r") as arquivo3:   
                    texto2 = json.load(arquivo3)
                    for obj in texto2:
                        s = Horario(obj["id"], obj["data"], obj["comfirmado"])                    
                        cls.horarios.append(s)
            except FileNotFoundError:
                pass
    
