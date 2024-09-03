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
    @classmethod
    def inserir(cls,obj):
        cls.abrir()
        m = 0
        for a in cls.alunos:
            if a.id > m: m = a.id
        obj.id = m + 1
        cls.alunos.append(obj)
        cls.salvar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.alunos
    
    @classmethod
    def salvar(cls): #salvar/criar arquivo .json
        with open("alunos.json", mode = 'w') as arquivo:
            json.dump(cls.alunos, arquivo, default = Aluno.json)

    
    @classmethod
    def abrir(cls):
        cls.alunos = []
        try:
            with open("alunos.json", mode = 'r') as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    a = Aluno()

                    cls.alunos.append(a)
        except FileNotFoundError:
            pass





