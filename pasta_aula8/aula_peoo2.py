import random

class Bingo:
    def __init__(self):
        self.__numbolas = 10
        self.__sorteados = []
    
    def iniciar(self,numbolas):
        if numbolas > 0:
            self.__numbolas = numbolas
        else:
            raise ValueError
        self.__sorteados.clear
    
    def proximo(self):
        if len(self.__sorteados) == self.__numbolas:
            return "Fim de jogo"
        n = random.randint(1,self.__numbolas)
        
        while n in self.__sorteados:
            n = random.randint(1,self.__numbolas)
            #print("Dentro do metodo:", n)
        
        self.__sorteados.append(n)
            #print(self.__sorteados)
        return n
    
    def sorteados(self):
        return sorted(self.__sorteados)

class UI:
    @staticmethod
    def menu():
        print("1 - iniciar jogo, 2 - proximo, 3 - sorteados, 4 - fim")
        return int(input("Escolha uma opção: "))
    
    @staticmethod
    def main():
        b = Bingo()
        print("Bem-vindo(a) ao if bingo")
        op = 0
        while op != 4:
            op = UI.menu()
            if op == 1:
                UI.iniciar_jogo(b)
            if op == 2:
                UI.proximo(b)
            if op == 3:
                UI.sorteados(b)
        print("Adeus")
    
    @staticmethod
    def iniciar_jogo(b):
        n = int(input("Informe o numero de bolas: "))
        b.iniciar(n)
    
    @staticmethod
    def proximo(b):
        print(b.proximo())
    
    @staticmethod
    def sorteados(b):
        print(b.sorteados())

UI.main()
