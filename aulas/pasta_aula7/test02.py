class Teste_encapsulamento:
    def __init__(self):
        self.__valor = 0
        self.__valor2 = 0
    
    def set_valor1(self, num):
        if num > 0:
            self.__valor = num
        else:
            raise ValueError
    
    def get_valor1(self):
        return self.__valor
    
    def set_valor2(self, num2):
        if num2 > 0:
            self.__valor2 = num2
        else:
            raise ValueError
    
    def get_valor2(self):
        return self.__valor2

    def calcular(self):
        return (self.__valor * self.__valor2)/2

class UI:
    @staticmethod
    def main():
        x = Teste_encapsulamento()
        x.set_valor1(int(input("Digite um valor: ")))
        x.set_valor2(int(input("Digite outro valor: ")))

        print(x.calcular())

UI.main()
        
        