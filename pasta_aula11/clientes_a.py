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
        cls.objetos.append(cliente)
    
    @classmethod
    def Listar (cls):
        return cls.objetos
    
    @classmethod
    def Salvar(cls):
        with open("clientes2.json", mode="w") as arquivo:
            json.dump()

    
class UI:
    @staticmethod
    def menu():
        print("")
        return int(input("Digite um número: "))
    

    
    