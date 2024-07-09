#Encapsulamento - aula 12
class Triangulo: #classe entidade
    
    def __init__(self): #Método construtor
        
        self.b = 0  #atributos
        self.h = 0
    
    def calc_area(self): #método
        return self.b * self.h / 2
    
class UI: #Classe de entrada e saida
    
    @staticmethod #Não é um objeto
    
    def main(): #Operação principal da UI
        
        x = Triangulo() #Entidade
        
        x.b = float(input("Informe o valor da base: "))
        x.h = float(input("Informe o valor da altura: "))
        print(x.calc_area())
    
UI.main() #Rodar o programa