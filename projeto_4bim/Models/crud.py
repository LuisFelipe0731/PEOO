from abc import ABC, abstractmethod

class CRUD(ABC):
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        for c in cls.objetos:
            try:
                if c.__id > m: m = c.__id
            except AttributeError:
                return f"valor invalido"
        obj.__id = m + 1
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
            if c.__id == id: return c
        return None  
    
    @abstractmethod
    def atualizar(cls, obj):
        pass

    @classmethod
    def excluir(cls, obj):
        c = cls.listar_id(obj.__id)
        if c != None:
            cls.objetos.remove(c)
        cls.salvar()
    

    @abstractmethod
    def abrir(cls):
        pass
    
    @abstractmethod
    def salvar(cls):
        pass