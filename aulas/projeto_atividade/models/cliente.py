import json

# Modelo
class Cliente:
  def __init__(self, id, nome, email, fone, senha):
    self.__id = 0
    self.__nome = ''
    self.__email = ''
    self.__fone = ''
    self.__senha = ''
    
    #set - atributos
    self.set_id(id)
    self.set_nome(nome)
    self.set_email(email)
    self.set_fone(fone)
    self.set_senha(senha)
  
  #set
  def set_id(self,id):
    if id != 0:
      self.__id = id
    else:
      raise ValueError

  def set_nome(self,nome):
    if nome != "":
      self.__nome = nome
    else:
      raise ValueError
  
  def set_email(self,email):
    if email != "":
      self.__email = email
    else:
      raise ValueError
  
  def set_fone(self,fone):
    if fone != "":
      self.__fone = fone
    else:
      raise ValueError
  
  def set_senha(self,senha):
    if senha != "":
      self.__senha = senha
    else:
      raise ValueError
  #get
  def get_id(self): return self.__id
  def get_nome(self): return self.__nome
  def get_email(self): return self.__email
  def get_fone(self): return self.__fone
  def get_senha(self): return self.__senha

  def __str__(self):
    return f"{self.__nome} - {self.__email} - {self.__fone}"

# Persistência
class Clientes:
  objetos = []    # atributo estático

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    m = 0
    for c in cls.objetos:
      if c.__id > m: m = c.__id
    obj.__id = m + 1
    cls.objetos.append(obj)
    cls.salvar()

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for c in cls.objetos:
      if c.__id == id: return c
    return None  
  
  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj.__id)
    if c != None:
      c.__nome = obj.__nome
      c.__email = obj.__email
      c.__fone = obj.__fone
      c.__senha = obj.__senha
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.__id)
    if c != None:
      cls.objetos.remove(c)
      cls.salvar()
  
  @classmethod
  def listar(cls):
    cls.abrir()
    cls.objetos.sort(key=lambda cliente: cliente.__nome)
    return cls.objetos

  @classmethod
  def salvar(cls):
    with open("clientes.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("clientes.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"], obj["senha"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass

