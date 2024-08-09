from datetime import datetime
from datetime import timedelta

#classes - musica e playlist
class Musica:
    def __init__(self, titulo, artista, album, data, duracao):
        if titulo == "": raise ValueError
        if artista == "": raise ValueError
        if album == "": raise ValueError
        if data == "": raise ValueError
        if duracao == "": raise ValueError
        
        self.__titulo = titulo
        self.__artista = artista  
        self.__album = album
        self.__datainclusao = data
        self.__duracao =  duracao
    
    def get_titulo(self): return self.__titulo
    def get_artista(self): return self.__artista
    def get_album(self): return self.__album
    def get_data(self): return self.__datainclusao
    def get_duracao(self): return self.__duracao
        

class Playlist:
    def __init__(self, nome, descricao):
        if nome == "": raise ValueError
        self.__nome = nome
        self.__descricao = descricao
        self.__musicas = []
    def inserir(self,m):
        self.__musicas.append(m)

    def listar(self):
        return self.__musicas[:]
    
    def tempo_total(self,t):
        
        return sum(self.__musicas)

    def __str__(self):
        return f"Playlist {self.__nome} -{self.__descricao} tem {len(self.__musicas)} músicas(s)"

#classe user interface
class UI:
    @staticmethod
    def menu():
        print("1 - Nova Playlist, 2 - Inserir Música, 3 - Listar Música, 4 - Info, 5 - Tempo Total, 6 - fim ")
        return int(input("Escolha uma opção: "))
    
    @staticmethod
    def main():
        print("Criador de Playlist")
        op = 0
        while op != 6:
            op = UI.menu()
            if op == 1:
                p = UI.nova_playlist()
            if op == 2:
                UI.inserir_musica(p)
            if op == 3:
                UI.listar_musica(p)
            if op == 4:
                UI.info(p)
            if op == 5:
                UI.tempo_total(p)
        print("FIM")
    @staticmethod
    def nova_playlist():
        nome = input("Informe o nome da playlist: ")
        desc = input("Escreva uma descrição para a playlist: ")
        p = Playlist(nome, desc)
        
        return p
    @staticmethod
    def inserir_musica(p):
        a = input("Informe o título da música: ")
        b = input("Informe o artista: ")
        c = input("Informe o álbum: ")
        d = input("Informe a data de inclusão(dd/mm/aaaa): ")
        y = datetime.strptime(d,"%d/%m/%Y")
        
        e = input("Informe a duração(mm:ss): ")
        x = e.split(":")
        min = int(x[0])
        seg = int(x[1])

        duracao1 = timedelta(minutes=min,seconds=seg)


        m = Musica(a,b,c,y,duracao1)
        p.inserir(m)

    @staticmethod
    def listar_musica(p):
        print("Músicas inseridas na playlist: ")
        for m in p.listar():
            print(m)

    @staticmethod
    def info(p):

    @staticmethod
    def tempo_total(p):


