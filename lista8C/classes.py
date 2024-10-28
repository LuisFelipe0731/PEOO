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
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.confirmado = False
        self.id_cliente = 0
        self.id_servico = 0
    def __str__(self):
        return f"{self.id} - {self.data.strftime('%d/%m/%Y %H:%M')}"
    def to_json(self):
        dic = {}
        dic["id"] = self.id
        dic["data"] = self.data.strftime('%d/%m/%Y %H:%M')
        dic["confirmado"] = self.confirmado
        dic["id_cliente"] = self.id_cliente
        dic["id_servico"] = self.id_servico
        return dic
      #return { "id" : {self.id}, "data" : {self.data}, "confirmado" : {self.confirmado}, "id_cliente" : {self.id_cliente}, "id_servico" : {self.id_servico}' }
    
class Horarios:
    objetos = []  # atributo estático
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0                     # cálculo do maior id utilizado - começa com 0
        for c in cls.objetos:     # percorre a lista de clientes - c é cada cliente
            if c.id > m: m = c.id   # compara o id de c com m (maior)
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
            c.data = obj.data
            c.confirmado = obj.confirmado
            c.id_cliente = obj.id_cliente
            c.id_servico = obj.id_servico
        cls.salvar()   
    @classmethod
    def excluir(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None: 
            cls.objetos.remove(c)
        cls.salvar()   
    @classmethod
    def salvar(cls):
        with open("horarios.json", mode = "w") as arquivo:   # write
            json.dump(cls.objetos, arquivo, default = Horario.to_json) 
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try: 
            with open("horarios.json", mode = "r") as arquivo:   # read
                texto = json.load(arquivo)
                for obj in texto:
                    c = Horario(obj["id"], datetime.strptime(obj["data"], "%d/%m/%Y %H:%M"))
                    c.confirmado = obj["confirmado"]
                    c.id_cliente = obj["id_cliente"]
                    c.id_servico = obj["id_servico"]
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass

#serviço