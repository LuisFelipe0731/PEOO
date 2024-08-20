import json

class Cliente: #Aula de crud
    def __init__(self, id, nome, email, fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
    def __str__(self):
        return f"{self.nome} - {self.id} - {self.email} - {self.fone}"    

class Clientes:
    objetos = []

    @classmethod
    def Inserir (cls, cliente):
        cls.Abrir()
        m = 0
        for c in cls.objetos:
            if c.id > m:
                m  = c.id
        cliente.id = m + 1
        cls.objetos.append(cliente)
        cls.Salvar()
    
    @classmethod
    def Listar (cls):
        cls.Abrir()
        return cls.objetos
    
    @classmethod
    def Salvar(cls):
        with open("clientes2.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)
    
    @classmethod
    def Abrir(cls):
        cls.objetos = []
        with open("clientes2.json", Mode="r") as arquivo:
            texto = json.load(arquivo)
            for obj in texto:
                



    
class UI:
    @staticmethod
    def menu():
        print("")
        return int(input("Digite um número: "))
    

    
    