class Agua:
    def __init__(self):
        self.__mes = 0
        self.__ano = 0
        self.__consumo = 0
    
    def set_consumo(self, consumo):
        if consumo >= 0:
            self.__consumo = consumo
        else:
            raise ValueError
    def get_consumo(self):
        return self.__consumo
   
    def set_data(self,data):
        t = data.split()
        self.__mes = int(t[0])
        self.__ano = int(t[1])
        if self.__mes <= 0 or self.__mes > 12 or self.__ano < 0 or self.__ano > 2024:
            raise ValueError
    def get_data(self):
        return f"{self.__mes}/{self.__ano}"
    
    def boleto(self):
        consumo_mim = 38.00
        if self.__consumo == 10:
            return consumo_mim
        
        if self.__consumo > 10 and self.__consumo <= 20:
            return consumo_mim + (self.__consumo * 5)
        
        elif self.__consumo >= 21:
            return consumo_mim + (self.__consumo * 6)

class UI:
    @staticmethod
    def main():
        x = Agua()
        x.set_consumo(int(input("Digite o consumo de agua: ")))
        x.set_data(input("Digite uma data: "))

        print(f"Sua conta é {x.boleto()} na data de {x.get_data()}")
UI.main()