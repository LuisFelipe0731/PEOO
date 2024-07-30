class Retagulo:
    def __init__(self,b,h):
        self.__b = 0
        self.__h = 0
        self.set_base(b)
        self.set_altura(h)
    
    def set_base(self,z):
        if z > 0:
            self.__b = z
        else:
            raise ValueError
    
    def get_base(self):
        return self.__b

    def set_altura(self,a):
        if a > 0:
            self.__h = a
        else:
            raise ValueError
    def get_altura(self):
        return self.__h
    
    def Calculo_area(self):
        return self.__h * self.__b
    def Calculo_diagonal(self):
        return (self.__b**2 + self.__h**2) **0.5
    
    def __str__(self):
        return f"Área: {self.Calculo_area}, Diagonal: {self.Calculo_diagonal}"

class Frete:
    def __init__(self,d,p):
        self.__d = 0
        self.__p = 0
        self.set_distancia(d)
        self.set_peso(p)
    
    def set_distancia(self,km):
        if km > 0:
            self.__d = km
        else:
            raise ValueError
    def get_distancia(self):
        return self.__d
    
    def set_peso(self,peso):
        if peso > 0:
            self.__p = peso
        else:
            raise ValueError
    def get_peso(self):
        return self.__p

    def calcular_frete(self):
        centavo = 0.01
        return centavo * (self.__p/self.__d)

    def __str__(self):
        return f"O frete: {self.calcular_frete}R$"

class Equacao_do_2_grau:
    def __init__(self,a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c
    
    def calcular_delta(self):
        return (self.__b**2) - (4 * self.__a * self.__c)
    
    def raiz1(self):
        return (-self.__b + (self.calcular_delta() ** 0.5)) / 2*self.__a
    
    def raiz2(self):
        return (-self.__b - (self.calcular_delta() ** 0.5)) / 2*self.__a


        
