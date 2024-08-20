class Cliente:
    def __init__(self, id, nome, email, fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
    def __str__(self):
        return f"{self.nome} - {self.id} - {self.email} - {self.fone}"    

class Clientes:
    def __init__(self):
        self.objetos = []

    def Inserir (self, cliente):
        self.objetos.append(cliente)
    
    def Listar (self):
        return self.objetos[:]