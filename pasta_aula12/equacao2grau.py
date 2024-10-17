import math

class Equacao2grau:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def __str__(self):
        return f"A = {self.a} B = {self.b} C = {self.c}"

    def Delta(self):
        return self.b ** 2 - (4 * self.a * self.c)

    def Tem_raiz(self):
        if self.Delta() > 0:
            return f"Possui duas raizes"
        if self.Delta() == 0:
            return f"Possui apenas uma raiz"
        else:
            return f"Nao possui raiz"
    
    def raiz1(self):
        return (-self.b - math.sqrt(self.Delta()))/ (2 * self.a)
    
    def raiz2(self):
        return (-self.b + math.sqrt(self.Delta()))/ (2 * self.a)

