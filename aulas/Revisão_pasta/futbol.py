class Jogador:
    def __init__(self):
        self.__nome = " "
        self.__camisa = " "
        self.__n_gols = 0
    
    def set_nome(self, a):
        if a != " ":
            self.__nome = a
        else:
            raise ValueError

    def set_camisa(self,num):
        if num != " ":
            self.__camisa = num
        else:
            raise ValueError
        
    def set_n_gols(self,gols):
        if gols >= 0:
            self.__n_gols = gols
        else:
            raise ValueError
    def get_nome(self): return self.__nome
    def get_camisa(self): return self.__camisa
    def get_gols(self): return self.__n_gols

    def __str__(self):
        return f"Nome:{self.__nome} - Camisa: {self.__camisa}"

class Time:
    def __init__(self,nome,estado):
        self.__nome = nome
        self.__estado = estado
        self.__jogadores = []
        if nome == " " or estado == " ":
            raise ValueError
    
    def Inserir_jogador1(self, j):
        self.__jogadores.append(j)
    
    def Listar_jogadores1(self):
        return self.__jogadores[:]

    def Artilheiro1(self):
        return max(self.__jogadores)

    def __str__(self):
        return f"O time {self.__nome}, do estado do {self.__estado} tem {len(self.__jogadores)} jogadores" 

        