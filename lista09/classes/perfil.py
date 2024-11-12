import json

class Perfil:
    def __init__(self, id, nome, desc, beneficio):
        self.id = id
        self.nome = nome
        self.desc = desc
        self.beneficio = beneficio
    def __str__(self):
        return f"{self.nome} - {self.desc} - {self.beneficio}"

class Perfis:
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
            c.desc = obj.desc
            c.beneficio = obj.beneficio
            
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
        cls.objetos.sort(key=lambda perfil: perfil.nome)
        return cls.objetos

    @classmethod
    def salvar(cls):
        with open("perfis.json", mode="w") as arquivo:   # w - write
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("perfis.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Perfil(obj["id"], obj["nome"], obj["desc"], obj["beneficio"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass
