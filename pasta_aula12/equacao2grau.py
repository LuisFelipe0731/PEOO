import math

class Equacao2grau:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    def __str__(self):
        return f"A = {self.__a} B = {self.__b} C = {self.__c}"

    def Delta(self):
        return self.__b ** 2 - (4 * self.__a * self.__c)

    def Tem_raiz(self):
        x = math.sqrt(self.Delta())
        if x > 0:
            return f"Possui duas raizes"
        if x == 0:
            return f"Possui apenas uma raiz"
        else:
            return f"Nao possui raiz"
    
    def raiz1(self):
        return -self.__b - (math.sqrt(self.Delta()))/ 2 * self.__a
    
    def raiz2(self):
        return -self.__b + (math.sqrt(self.Delta()))/ 2 * self.__a

