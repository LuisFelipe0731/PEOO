import json
from abc import ABC, abstractmethod

class CRUD(ABC):
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
            c.senha = obj.senha
            c.id_perfil = obj.id_perfil
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
        cls.objetos.sort(key=lambda objeto: objeto.nome)
        return cls.objetos

    @abstractmethod
    def abrir(cls):
        pass
    
    @abstractmethod
    def salvar(cls):
        pass