class Conta_banco:
    def __init__(self):
        self.__titular = ''
        self.__numero_conta = 0
        self.__saldo = 0
    
    def set_titular(self, nome):
        self.__titular = nome
    def get_titluar(self):
        return self.__titular
    def set_numero_conta(self,num):
        if num > 0:
            self.__numero_conta = num
        else:
            raise ValueError
    def get_numero_conta(self):
        return self.__numero_conta

    def depositar(self, y):
        if y >= 0:
            self.__saldo += y  
    def saque(self, saque):
        if saque >= 0:
            self.__saldo -= saque

class Viagem2:
    def __init__(self):
        self.__destino = ''
        self.__distancia = 0
        self.__litros = 0
    
    def set_destino(self, local): #localização
        self.__destino = local
        if local == '':
            raise ValueError
    def get_destino(self):
        return self.__destino

    def set_distancia(self, km): #distancia
        if km > 0:
            self.__distancia = km
        else:
            raise ValueError
    def get_distancia(self):
        return self.__distancia
        
    def set_litros(self, litro): #litros
        if litro > 0:
            self.__litros = litro
        else:
            raise ValueError
    def get_litros(self):
        return self.__litros

    def Calculo(self):
        return self.__distancia / self.__litros

class UI:
    @staticmethod
    def main():
        x = Viagem2()
       
        x.set_destino((input("Digite seu destino: ")))
        x.set_distancia(int(input("Digite a distancia: ")))
        x.set_litros(int(input("Digite litros: ")))

        print(x.Calculo())
    
         

        
UI.main()