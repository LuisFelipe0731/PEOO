import json
from datetime import datetime

class Horario:
    def __init__(self, id, data):
        self.__id = ''
        self.__data = ''
        self.__confirmado = False
        self.__id_cliente = 0
        self.__id_servico = 0

    #set
    def set_id(self,id):
      if id != 0:
        self.__id = id
      else:
        raise ValueError

    def set_data(self,data):
      if data != "":
        self.__data = datetime.strptime(data,"%d/%m/%Y %H:%M")
      else:
        raise ValueError
    #get
    def get_id(self): return self.__id
    def get_nome(self): return self.__data
    def get_email(self): return self.__confirmado
    def get_fone(self): return self.__id_cliente
    def get_senha(self): return self.__id_servico
      
    def __str__(self):
        return f"{self.__id} - {self.__data}"
    def to_json(self):
      dic = {}
      dic["id"] = self.__id
      dic["data"] = self.__data.strftime("%d/%m/%Y %H:%M")
      dic["confirmado"] = self.__confirmado
      dic["id_cliente"] = self.__id_cliente
      dic["id_servico"] = self.__id_servico
      return dic    

class Horarios:
  objetos = []    # atributo estático

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
  def listar(cls):
    cls.abrir()
    return cls.objetos
  
  @classmethod
  def salvar(cls):
    with open("horarios.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = Horario.to_json)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("horarios.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Horario(obj["id"], datetime.strptime(obj["data"], "%d/%m/%Y %H:%M"))
          c.confirmado = obj["confirmado"]
          c.id_cliente = obj["id_cliente"]
          c.id_servico = obj["id_servico"]
          cls.objetos.append(c)
    except FileNotFoundError:
      pass



