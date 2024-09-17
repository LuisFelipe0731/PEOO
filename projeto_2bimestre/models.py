#classes
#Professor
class Professsor:
    def __init__(self, id, nome, diretoria, materia):
        self.id = id
        self.nome = nome
        self.diretoria = diretoria
        self.materia = materia
    def __str__(self):
        return f""

#Curso
class Curso:
    def __init__(self, id, nome, diretoria, tempo_de_conclusao):
        self.id = id
        self.nome = nome
        self.diretoria = diretoria
        self.t = tempo_de_conclusao
    def __str__(self):
        return f""
    
    def to_json(self):
        dic = {}
        
        dic["id"] = self.id
        dic["nome"] = self.nome
        dic["diretoria"] = self.diretoria
        dic["tempo de conclusâo"] = self.t.strftime('%d/%m/%Y %H:%M')
        return dic

#Diretoria
class Diretoria:
    def __init__(self, id, nome, cursos):
        self.id = id
        self.nome = nome
        self.cursos = cursos
        self.id_professor = 0
        self.id_curso = 0
    def __str__(self):
        return f""