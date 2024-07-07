class Triangulo:
    def __init__(self):
        self.h = 0
        self.b = 0
    
    def Area_tri(self):
        return (self.b * self.h)/2

junior = Triangulo()
junior.h = 60
junior.b = 67

print(junior.Area_tri())

class Circulo:
    def __init__(self):
        self.raio = 0
        self.pi = 3.14
    
    def area_circ(self):
        return (self.pi *(self.raio**2))

    def circunferencia(self):
        return (2 * self.pi * self.raio)

class Conta_banco:
    def __init__(self):
        self.titular = ''
        self.saldo = 0
        self.num_conta = ''
    
    def Deposistar(self,num):
        self.saldo += num
    
    def Saque(self,saque):
       self.saldo -= saque




