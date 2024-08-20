import json

class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def __str__(self):
        return f"{self.id} - {self.nome}"
    
a = Cliente(2215, "Eduardo")
b = Cliente(445641, "Cavalo")

lista = [a,b]
with open("Clientes.json", mode = "w") as arquivo:
    json.dump(lista,arquivo,default = vars)