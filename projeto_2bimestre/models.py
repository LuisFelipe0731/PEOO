#classes
#Professor
class Professsor:
    def __init__(self, id, nome, diretoria, materia):
        self.id = id
        self.nome = nome
        self.diretoria = diretoria
        self.materia = materia

#Curso
class Curso:
    def __init__(self, id, nome, diretoria, tempo_de_conclusao):
        self.id = id
        self.nome = nome
        self.diretoria = diretoria
        self.t = tempo_de_conclusao

#Diretoria
class Diretoria:
    def __init__(self, id, nome, cursos):
        self.id = id
        self.nome = nome
        self.cursos = cursos