from models import *
#view

#Professores
def Professor_inserir(nome,diretoria, materia):
    Professores.inserir(Professor(0,nome,diretoria, materia))

def Listar_professor():
    return Professores.listar()

def Atualizar_professor(id,nome, diretoria, materia):
    c = Professor(id,nome,diretoria,materia)
    Professores.atualizar(c)

def Excluir_professor(id):
    c = Professor(id, "", "", "")
    Professores.excluir(c)


#Cursos
def curso_inserir(nome,diretoria, data):
    Cursos.inserir(Curso(0,nome,diretoria, data))

def Listar_curso():
    return Cursos.listar()

def Atualizar_curso(id, nome, diretoria, data):
    c = Curso(id,nome,diretoria,data)
    Cursos.atualizar(c)

def Excluir_curso(id):
    c = Curso(id, "", "", "")
    Cursos.excluir(c)

#Diretoria
def diretoria_inserir(nome):
    Diretorias.inserir(Diretoria(0,nome))

def Listar_diretoria():
    return Diretorias.listar()

def Atualizar_diretoria(id, nome):
    c = Diretoria(id,nome)
    Diretorias.atualizar(c)

def Excluir_diretoria(id):
    c = Diretoria(id,"")
    Diretorias.excluir(c)