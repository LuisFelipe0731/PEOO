#Encapsulamento - aula 12
class Triangulo: #classe entidade
    
    def __init__(self): #Método construtor
        
        self.__b = 0  #atributos encapsulados
        self.__h = 0
    def set_b(self, valor): # Set e Get
        if valor >= 0:
            self.__b = valor
    def get_b(self):
        return self.__b
    
    def set_h(self, valor): 
        if valor >= 0:
            self.__b = valor
    def get_h(self):
        return self.__b
    
    def calc_area(self): #método
        return self.__b * self.__h / 2
    
    
class UI: #Classe de entrada e saida
    
    @staticmethod #Não é um objeto
    
    def main(): #Operação principal da UI
        
        x = Triangulo() #Entidade
        
        x.b = float(input("Informe o valor da base: "))
        x.h = float(input("Informe o valor da altura: "))
        print(x.calc_area())
    
UI.main() #Rodar o programa