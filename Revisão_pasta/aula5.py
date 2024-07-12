#encapsulamento 2
class Corrida:
    def _init__(self):
        self.__distancia = 1
        self.__horas = 0
        self.__minutos = 0
        self.__segundos = 0
    def set_distancia(self,distancia):
        if distancia > 0:
            self.__distancia = distancia
        else:
            raise ValueError
    def get_distancia(self):
        return self.__distancia
    def set_tempo(self, tempo):
        t = tempo.split(':')
        self.__horas = int(t[0])
        self.__minutos = int(t[1])
        self.__segundos = int(t[2])
        if self.__horas < 0 or self.__minutos < 0 or self.__segundos < 0:
            raise ValueError
    def get_tempo(self):
        return f"{self.__horas}:{self.__minutos}:{self.__segundos}"
    def pace(self):
        t = self.__horas * 60 + self.__minutos + self.__segundos/60
        d = self.__distancia/1000
        return t/d

class UI:
    @staticmethod
    def main():
        y = Corrida()
        y.set_distancia(int(input()))
        y.set_tempo(input())
        print(y.pace())
UI.main()