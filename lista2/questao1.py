class Viagem:
    def __init__(self):
        self.__km = 0
        self.__horas = 0
        self.__minutos = 0
    def set_km(self, distancia):
        if distancia > 0:
            self.__km = distancia
        else:
            raise ValueError
    def get_km(self):
        return self.__km
    def set_tempo(self, tempo):
        t = tempo.split()
        self.__horas = int(t[0])
        self.__minutos = int(t[1])
        if self.__horas < 0 or self.__minutos < 0 or self.__horas + self.__minutos == 0:
            raise ValueError
    def get_tempo(self):
        return f"{self.__horas}:{self.__minutos}"
    def Velocidade_media(self):
        tt = self.__horas + (self.__minutos/60)
        return self.__km/tt




class UI:
    @staticmethod
    
    def main():
        x = Viagem() 
        
        x.set_km(float(input("Informe a distantica da viagem: ")))
        x.set_tempo(input("Informe o tempo da viagem: "))
        print(x.get_km())
        print(x.Velocidade_media())
       
        
    
UI.main()