import json
import datetime

#classe paciente
class Paciente:
    def __init__(self,id,nome,fone,nasc):
        self.__id = 0
        self.__nome = ""
        self.__fone = ""
        self.__nasc = ""
        self.set_id(id)
        self.set_nome(nome)
        self.set_fone(fone)
        self.set_nasc(nasc)

    def set_id(self,x):
        if x > 0: self.__id = x
        else: raise ValueError
    def set_nome(self,n):
            if n != "": self.__nome = n
            else: raise ValueError
    def set_fone(self,f):
            if f != "": self.__fone = f
            else: raise ValueError
    def set_nasc(self,data):
            if data != "": self.__nasc = data
            else: raise ValueError
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_fone(self): return self.__fone
    def get_nasc(self): return self.__nasc
    
    
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.fone} - {self.nasc.strftime("%d/%m/%Y")}"
    
class Pacientes:
    pacientes = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0                     
        for p in cls.pacientes:     
            if p.id > m: m = p.id   
        obj.id = m + 1  
        cls.objetos.append(obj)
        cls.salvar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.pacientes
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for p in cls.pacientes:
            if p.id == id: return p
        return None 
    
    @classmethod
    def atualizar(cls, obj):
        p = cls.listar_id(obj.id)
        if p != None:
            p.nome = obj.nome
            p.email = obj.email
            p.fone = obj.fone
        cls.salvar()   
    
    @classmethod
    def excluir(cls, obj):
        p = cls.listar_id(obj.id)
        if p != None: 
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
                    c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])                     # dicionário
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass
          
class UI:
        
        