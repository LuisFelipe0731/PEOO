class Circulo:
    def __init__(self):
        self.__raio = 0
        self.__pi = 3.14
    
    def set_raio(self,valor):
        if valor > 0:
            self.__raio = valor
        else:
            raise ValueError
    
    def get_raio(self):
        return self.__raio
    
    def Area_circ(self):
        return (self.__pi *(self.__raio**2))

    def Circunferencia(self):
        return (2 * self.__pi * self.__raio)




class UI:
    @staticmethod
    
    def main():