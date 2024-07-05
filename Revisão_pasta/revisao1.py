#aula 11 - revisão
#re-introdução à POO
class triangulo: #Classe
    def __init__(self):
        self.b = 0
        self.h = 0
    def calc_area(self):
        return self.b * self.h/2
    
ju = triangulo() #Objeto

ju.h = 3
ju.b = 5

print(ju.calc_area())\
