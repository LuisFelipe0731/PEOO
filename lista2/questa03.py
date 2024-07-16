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
    
         

        