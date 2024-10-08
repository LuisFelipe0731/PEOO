import json
import datetime

#classe paciente
class Paciente:
    def __init__(self,id,nome,fone,nasc):
        self.id = id
        self.nome = nome
        self.fone = fone
        self.nasc = nasc
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.fone} - {self.nasc.strftime('%d/%m/%M')}"
    def to_json(self):
        dic = {}
        dic["id"] = self.id  
        dic["nome"] = self.nome 
        dic["fone"] = self.fone 
        dic["nascimento"] = self.nasc.strftime('%d/%m/%Y')   
        return dic

class Pacientes: #Lista de Objetos
    pacientes = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0                     
        for p in cls.pacientes:      
            if p.id > m: m = p.id   
        obj.id = m + 1  
        cls.pacientes.append(obj)
        cls.salvar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.pacientes
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for p in cls.pacientes:
            if p.id == id: return p
        return None 
    @classmethod
    def atualizar(cls, obj):
        p = cls.listar_id(obj.id)
        if p != None:
            p.nome = obj.nome
            p.fone = obj.fone
            p.nasc = obj.nasc
        cls.salvar()   
    
    @classmethod
    def excluir(cls, obj):
        p = cls.listar_id(obj.id)
        if p != None: 
            cls.pacientes.remove(p)
        cls.salvar()   
    
    @classmethod
    def salvar(cls):
        with open("pacientes.json", mode = "w") as arquivo:   # write
            json.dump(cls.pacientes, arquivo, default = Paciente.to_json) 
    
    @classmethod
    def abrir(cls):
        cls.pacientes = []
        try: 
            with open("pacientes.json", mode = "r") as arquivo:   # read
                texto = json.load(arquivo)
                for obj in texto:
                    p = Paciente(obj["id"], obj["nome"], obj["fone"],datetime.datetime.strptime(obj["nascimento"], "%d/%m/%Y"))

                    cls.pacientes.append(p)
        except FileNotFoundError:
            pass
    
class UI:
    @staticmethod
    def menu():
        print("Cadastro de Pacientes")
        print("  1 - Inserir, 2 - listar, 3 - atualizar, 4 - excluir, 5 - Fim")
        return int(input("Informe uma opção: "))

    @staticmethod
    def main():
        op = 0
        while op != 5:
            op = UI.menu()
            if op == 1: UI.paciente_inserir()
            if op == 2: UI.paciente_listar()
            if op == 3: UI.atualizar_paciente()
            if op == 4: UI.excluir_paciente()
    
    @staticmethod
    def paciente_inserir():
        id = int(input("Digite o id: "))
        nome = input("Digite o nome: ")
        fone = input("Digite o telefone: ")
        t = input("Informe a data de nascimento (dd/mm/aaaa):")
        nasc = datetime.datetime.strptime(t,"%d/%m/%Y")
        p = Paciente(id, nome, fone, nasc)
        Pacientes.inserir(p)
    
    @staticmethod
    def paciente_listar():
        for p in Pacientes.listar():
            print(p)
    
    @staticmethod
    def atualizar_paciente():
        UI.paciente_listar()
        id = int(input("Informe o id do paciente a ser atualizado: "))
        nome = input("Novo nome: ")
        fone = input("Novo telefone: ")
        t = input("Nova data de nascimento (dd/mm/aaaa): ")
        nasc = datetime.datetime.strptime(t,"%d/%m/%Y")
        p = Paciente(id,nome,fone,nasc)

        Pacientes.atualizar(p)

    def excluir_paciente():
        UI.paciente_listar()
        id = int(input("Informe o id do paciente a ser excluido: "))
        p = Paciente(id,"","","")
        Pacientes.excluir(p)

UI.main()

        
