import json
import datetime

#classe paciente
class Paciente:
    def __init__(self,id,nome,fone,nasc):
        self.id = id
        self.nome = nome
        self.fone = fone
        self.nasc = nasc
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.fone} - {self.nasc.strftime('%d/%m/%M')}"
        