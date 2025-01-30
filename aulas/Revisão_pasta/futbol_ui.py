from futbol import *

class UI:
    @staticmethod
    def menu():
        print("1 - Novo time, 2 - Inserir Jogador, 3 - Listar Jogadores, 4 - Mostrar artilheiro, 5- fim ")
        return int(input("Escolha uma das opções: "))
    
    @staticmethod
    def main():
        print("Bem-vindo(a) ao formador de time 2000")

        num = 0
        while num != 5:
            num = UI.menu()
            if num == 1:
                time = UI.Novo_time()
            if num == 2:
                UI.Inserir_jogador(time)
            if num == 3:
                UI.Listar_jogadores(time)
            if num == 4:
                UI.Mostrar_artilheiro(time)
        print("Fim")
    
    @staticmethod
    def Novo_time():
        nome = input("Digite o nome do time: ")
        estado = input("Digite o estado do time: ")
        time = Time(nome, estado)
        return time
    
    @staticmethod
    def Inserir_jogador(time):
        nome = input("Digite o nome do jogador: ")
        camisa = input("Digite o número da camisa: ")
        gols = input("Digite o número de gols: ")

        j = Jogador()
        j.set_nome(nome)
        j.set_camisa(camisa)
        j.set_n_gols(gols)
        
        time.Inserir_jogador1(j)
    
    @staticmethod
    def Listar_jogadores(time):
        print("Jogadores inseridos: ")
        for j in time.Listar_jogadores1():
            print(j)

    @staticmethod
    def Mostrar_artilheiro(time):
        print("Artilheiro do time: ")
        print(time.Artilheiro1())

UI.main()

