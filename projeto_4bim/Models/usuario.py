import json
from Models.crud import CRUD

class Usuario:
    def __init__(self,id,nome, email, senha):
        self.__id = 0
        self.__nome = ""
        self.__email = ""
        self.__senha = ""

        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_senha(senha)


    #set e get
    def set_id(self,id):
        if id != 0:
            self.__id = id
        else:
            raise ValueError("Valor invalido")

    def set_nome(self,n):
        if n != "":
            self.__nome = n
        else:
            raise ValueError("O Usuario precisa ter um nome")
    
    def set_email(self,e):
        if e!= "":
            self.__email = e
        else:
            raise ValueError("O Usuario precisa ter um email")
    
    def set_senha(self,s):
        if s != "":
            self.__senha = s
        else:
            raise ValueError("O Usuario precisa de uma senha")
        
    #get
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_senha(self): return self.__senha

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email}"
    #to_json
    def to_json(self):
        dic = {}
        dic['id'] = self.__id  
        dic['nome'] = self.__nome
        dic['email'] = self.__email
        dic['senha'] = self.__senha
        return dic


class Usuarios(CRUD):
    def atualizar(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            c.__nome = obj.__nome
            c.__email = obj.__email
            c.__senha = obj.__senha  
        cls.salvar()
        
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Usuarios.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Usuario(obj['id'], obj['nome'], obj['email'], obj['senha'])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass
    
    @classmethod
    def salvar(cls):
        with open("Usuarios.json", mode="w") as arquivo:   # w - write
            json.dump(cls.objetos, arquivo, default = Usuario.to_json)
    
    