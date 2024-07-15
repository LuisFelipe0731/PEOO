class Viagem:
    def __init__(self):
        self.km = 0
        self.horas = 0
        self.minutos = 0
    def Velocidade(self):
        t = self.horas + (self.minutos/60)
        return self.km/t




class UI:
    @staticmethod
    
    def main():
        x = Viagem() 
        
        x.set_raio(float(input("Informe o valor do raio: ")))
       
        print(x.Area_circ())
        print(x.Circunferencia())
    
UI.main()