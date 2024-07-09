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

class Viagem:
    def __init__(self):
        self.km = 0
        self.horas = 0
        self.minutos = 0
    def Velocidade(self):
        t = self.horas + (self.minutos/60)
        return self.km/t
class Cinema:
    def __init__(self):
        self.horario = 0
        self.dia = ''

dudu = Conta_banco()
dudu.titular = 'Eduardo'
dudu.num_conta = '5505043'
dudu.Deposistar(500)
dudu.Saque(90)
print(dudu.titular)
print(dudu.num_conta)
print(dudu.saldo)


