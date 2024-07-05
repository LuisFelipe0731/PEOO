#aula 11 - revisão
#re-introdução à POO
class Triangulo: #Classe
    def __init__(self):
        self.b = 0
        self.h = 0
    def Calc_area(self):
        return self.b * self.h/2
    
class Aluno:
    def __init__(self):
        self.nome = ""
        self.matricula = ""
        self.email = ""
