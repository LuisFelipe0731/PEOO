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
