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
    def to_json(self):
        dic = {}
        dic["id"] = self.id  
        dic["nome"] = self.nome 
        dic["fone"] = self.fone 
        dic["nascimento"] = self.nasc   
        return dic

class Pacientes: #Lista de Objetos
    pacientes = []

    @classmethod
    def inserir(cls,obj):
        cls.abrir()