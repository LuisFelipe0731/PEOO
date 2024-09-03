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
        dic["matricula"] = self.matricula
        dic["nome"] = self.nome
        dic["curso"] = self.curso
        dic["data de matricula"] = self.data_de_matricula.strftime('%d/%m/%Y')
        return dic

class Alunos: #Lista de Objetos
    alunos = []
    

