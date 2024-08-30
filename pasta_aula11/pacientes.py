import json
import datetime

#classe paciente
class Paciente:
    def __init__(self,id,nome,fone,nasc):
        self.id = id
        self.nome = nome
        self.fone = fone
        self.nasc = nasc
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.fone} - {self.nasc.strftime('%d/%m/%M')}"
    def to_json(self):
        dic = {}
        dic["id"] = self.id  
        dic["nome"] = self.nome 
        dic["fone"] = self.fone 
        dic["nascimento"] = self.nasc   
        return dic

class Pacientes: #Lista de Objetos
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
       
        cls.salvar()   
    @classmethod
    def excluir(cls, obj):
        p = cls.listar_id(obj.id)
        if p != None: 
        cls.pacientes.remove(p)
        cls.salvar()   
    @classmethod
    def salvar(cls):
        with open("pacientes.json", mode = "w") as arquivo:   # write
            json.dump(cls.objetos, arquivo, default = Paciente.to_json) 
    @classmethod
    def abrir(cls):
        cls.pacientes = []
        try: 
            with open("pacientes.json", mode = "r") as arquivo:   # read
                texto = json.load(arquivo)
                for obj in texto:
                    p = Paciente(obj["id"], datetime.strptime(obj["nascimento"], "%d/%m/%Y %H:%M"))

                    cls.objetos.append(c)
        except FileNotFoundError:
            pass
    