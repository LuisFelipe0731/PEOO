class Conta_banco:
    def __init__(self):
        self.__titular = ''
        self.__numero_conta = 0
        self.__saldo = 0
    
    def set_titular(self, nome):
        self.__titular = nome
    def get_titluar(self):
        return self.__titular

        