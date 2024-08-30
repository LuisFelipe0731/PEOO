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
    