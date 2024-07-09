#Encapsulamento - aula 12
class Triangulo: #classe entidade
    def __init__(self):
        self.b = 0  #atributos
        self.h = 0
    def calc_area(self): #metodo
        return self.b * self.h / 2
    
class UI: #Classe de entrada e saida
    @staticmethod
    def main():
        x = Triangulo()
        x.b = 10
        x.h = 20
        print(x.calc_area())
    
UI.main()