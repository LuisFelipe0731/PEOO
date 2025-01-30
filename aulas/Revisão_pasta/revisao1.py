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

class Corrida:
    def __init__(self):
        self.dist = 1 #metros
        self.horas = 0
        self.minutos = 0
        self.segundos = 0
    def Pace(self):
        t = self.horas * 60 + self.minutos + self.segundos / 60
        d = self.dist / 1000
        return t/d
    
c = Corrida()

c.dist = float(input("Distancia: "))
c.horas = int(input())
c.minutos = int(input())
c.segundos = int(input())
print(c.Pace())