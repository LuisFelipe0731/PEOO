import json
import datetime

class Aluno: #objeto
    def __init__(self,matri,nome,curso,data):
        self.matricula = matri
        self.nome = nome
        self.curso = curso
        self.data_de_matricula = data
    def __str__(self):
        return f"{self.matricula} - {self.nome} - {self.curso} - {self.data_de_matricula}"

    def json(self):
        dic = {}
        
