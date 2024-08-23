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
    
    def __str__(self):
        return f"{self.id} - {self.data} - {self.comfirmado}"
        
        

class Serviço:
   def __init__(self,id,descricao,valor,tempo):
      self.id = id
      self.desc = descricao
      self.valor = valor
      self.t = tempo

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

class Horarios:
   