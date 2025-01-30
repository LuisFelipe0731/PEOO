from view import *
from datetime import datetime
#User Interface
class UI:
    @staticmethod
    def Menu():
        print("Professores: 1 - Inserir, 2 - listar, 3 - atualizar, 4 - excluir")
        print("Cursos: 5 - Inserir, 6 - listar, 7 - atualizar, 8 - excluir")
        print("Diretorias: 9 - Inserir, 10 - listar, 11 - atualizar, 12 - excluir")
        print("Outros: 13 - fim")
        return int(input("Informe uma opção: "))

    def Main():
        op = 0
        while op != 13: 
            op = UI.Menu()
            #Professores - funçoes
            if op == 1: UI.professor_inserir()
            if op == 2: UI.professor_listar()
            if op == 3: UI.professor_atualizar()
            if op == 4: UI.professor_excluir()
            #Cursos - funçoes
            if op == 5: UI.curso_inserir()
            if op == 6: UI.curso_listar()
            if op == 7: UI.curso_atualizar()
            if op == 8: UI.curso_excluir()
            #Diretorias - funçoes
            if op == 9: UI.diretoria_inserir()
            if op == 10: UI.diretoria_listar()
            if op == 11: UI.diretoria_atualizar()
            if op == 12: UI.diretoria_excluir()
        
    #Professores
    @staticmethod
    def professor_inserir():
        n = input("Informe o nome do professor: ")
        dire = input("Informe a diretoria: ")
        materia = input("Informe a materia: ")
        Professor_inserir(n,dire,materia)
    
    @staticmethod
    def professor_listar():
        for c in Listar_professor():
            print(c)
    
    @staticmethod
    def professor_atualizar():
        UI.professor_listar()
        id = int(input("Informe o id do professor a ser atualizado: "))
        n = input("novo nome: ")
        dire = input("nova diretoria: ")
        materia = input("nova materia: ")
        Atualizar_professor(id,n,dire,materia)

    @staticmethod
    def professor_excluir():
        UI.professor_listar()
        id = int(input("Informe o id do professor a ser excluido: "))
        Excluir_professor(id)
    
    #Cursos
    @staticmethod
    def curso_inserir():
        n = input("Informe o nome do curso: ")
        dire = input("Informe a diretoria: ")
        d = input("Informe a data de conclusao do curso(dd/mm/aaaa): ")
        data = datetime.strptime(d, "%d/%m/%Y")
        curso_inserir(n,dire,data)
    
    @staticmethod
    def curso_listar():
        for c in Listar_curso():
            print(c)
    
    @staticmethod
    def curso_atualizar():
        UI.curso_listar()
        id = int(input("Informe o id do curso a ser atualizado: "))
        n = input("novo nome: ")
        dire = input("nova diretoria: ")
        d = input("Informe a nova data de conclusao do curso(dd/mm/aaaa): ")
        data = datetime.strptime(d, "%d/%m/%Y")

        Atualizar_curso(id,n,dire,data)

    @staticmethod
    def curso_excluir():
        UI.curso_listar()
        id = int(input("Informe o id do curso a ser excluido: "))
        Excluir_curso(id)
    
    #Diretorias
    @staticmethod
    def diretoria_inserir():
        n = input("Informe o nome do diretoria: ")
        diretoria_inserir(n)
    
    @staticmethod
    def diretoria_listar():
        for c in Listar_diretoria():
            print(c)
    
    @staticmethod
    def diretoria_atualizar():
        UI.diretoria_listar()
        id = int(input("Informe o id do diretoria a ser atualizado: "))
        n = input("novo nome: ")
        Atualizar_diretoria(id,n)

    @staticmethod
    def diretoria_excluir():
        UI.diretoria_listar()
        id = int(input("Informe o id do diretoria a ser excluido: "))
        Excluir_diretoria(id)


UI.Main()