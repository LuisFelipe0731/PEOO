import datetime

class Paciente:
    def __init__(self, nome, cpf, telefone, nasc):
        self.__nome = " "
        self.__cpf = " "
        self.__telefone = " "
        self.__nasc = " "
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_telefone(telefone)
        self.set_nascimento(nasc)

    
    def set_nascimento(self, data):
        if data != "":
            self.__nasc = datetime.datetime.strptime(data, "%d/%m/%Y")
        else:
            raise ValueError
    
    def set_nome(self, nome):
        if nome != " ":
            self.__nome = nome
        else:
            raise ValueError
    def set_cpf(self, cpf):
        if cpf != " ":
            self.__cpf = cpf
        else:
            raise ValueError
    def set_telefone(self, tele):
        if tele != " ":
            self.__telefone = tele
        else:
            raise ValueError
    def get_data(self): return self.__nasc
    def get_nome(self): return self.__nome
    def get_cpf(self): return self.__cpf
    def get_telefone(self): self.__telefone

    def idade(self):
        hoje = datetime.datetime.today()

        return ((hoje - self.__nasc)//365)
    
    def __str__(self):
        return f"data de nascimento: {self.__telefone} nome: {self.__nome} cpf: {self.__cpf} telefone: {self.__telefone}"

class UI:
    @staticmethod
    def main():
        y = input("Digite seu nome: ")
        z = input("Digite seu cpf: ")
        r = input("Digite seu telefone: ")
        c = input("Digite sua data de nascimento(dd/mm/aaaa):")
        
        x = Paciente(y,z,r,c)
        
        print(x.idade())

UI.main()
