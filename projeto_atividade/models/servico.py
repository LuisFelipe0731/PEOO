import json

# Modelo
class Servico:
  def __init__(self, id, descricao, valor, duracao):
    self.__id = 0
    self.__descricao = ""
    self.__valor = ""
    self.__duracao = ""
  
  #set
  def set_id(self,id):
    if id != 0:
      self.__id = id
    else:
      raise ValueError

  def set_descri(self,descricao):
    if descricao != "":
      self.__data = descricao
    else:
      raise ValueError
  
  def set_valor(self,valor):
    if valor != "":
      self.__data = valor
    else:
      raise ValueError
  
  def set_duracao(self,duracao):
    if duracao != "":
      self.__data = duracao
    else:
      raise ValueError
  #get
  def get_id(self): return self.__id
  def get_descricao(self): return self.__descricao
  def get_valor(self): return self.__valor
  def get_duracao(self): return self.__duracao


  def __str__(self):
    return f"{self.__id} - {self.__descricao} - R$ {self.__valor:.2f} - {self.__duracao} min"

# Persistência
class Servicos:
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
      c.descricao = obj.descricao
      c.valor = obj.valor
      c.duracao = obj.duracao
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
    with open("servicos.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("servicos.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Servico(obj["id"], obj["descricao"], obj["valor"], obj["duracao"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass

