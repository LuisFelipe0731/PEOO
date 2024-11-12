import json

class Perfil:
    def __init__(self, id, nome, desc, beneficio):
        self.id = id
        self.nome = nome
        self.desc = desc
        self.beneficio = beneficio
    def __str__(self):
        return f"{self.nome} - {self.desc} - {self.beneficio}"
