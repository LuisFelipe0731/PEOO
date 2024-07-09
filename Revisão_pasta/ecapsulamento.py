#Encapsulamento - aula 12
class Triangulo:
    def __init__(self):
        self.b = 0  #atributos
        self.h = 0
    def calc_area(self): #metodo
        return self.b * self.h / 2