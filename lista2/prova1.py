import json
import datetime

class Avaliacao: #Objeto
    def __init__(self,id,disci,local,data):
        self.id = id
        self.disciplina = disci
        self.local = local
        self.data = data        
    
    def __str__(self):
        return f"{self.id} - {self.disciplina} - {self.local} - {self.data}"   

    def to_json(self):
        dic = {}
        dic["id"] = self.id
        dic["disciplina"] = self.disciplina
        dic["local"] = self.local
        dic["data"] = self.data.strftime('%d/%m/%Y')
        return dic     

class Avaliacoes:
    avaliacoes = []
    
    @classmethod
    def inserir(cls,obj):
        cls.abrir()
        m = 0
        for a in cls.avaliacoes:
            if a.id > m: m = a.id
        obj.id = m + 1
        cls.avaliacoes.append(obj)
        cls.salvar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.avaliacoes

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for a in cls.avaliacoes:
            if a.id == id: return a
        return None 
    
    @classmethod
    def atualizar(cls, obj):
        a = cls.listar_id(obj.id)
        if a != None:
            a.disciplina = obj.disciplina
            a.local = obj.local
            a.data = obj.data
        cls.salvar()   
    
    @classmethod
    def excluir(cls, obj):
        a = cls.listar_id(obj.id)
        if a != None: 
            cls.avaliacoes.remove(a)
        cls.salvar()
    
    @classmethod
    def salvar(cls): #salvar/criar arquivo .json
        with open("avaliacoes.json", mode = 'w') as arquivo:
            json.dump(cls.avaliacoes, arquivo, default = Avaliacao.to_json)

    
    @classmethod
    def abrir(cls): #abrir arquivo .json
        cls.avaliacoes = []
        try:
            with open("avaliacoes.json", mode = 'r') as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    a = Avaliacao(obj["id"], obj["disciplina"], obj["local"], datetime.datetime.strptime(obj["data"], '%d/%m/%Y'))

                    cls.avaliacoes.append(a)
        except FileNotFoundError:
            pass

class UI:
    @staticmethod
    def menu():
        print("Cadastro de Avaliações")
        print("  1 - Inserir, 2 - listar, 3 - atualizar, 4 - excluir, 5 - Fim")
        return int(input("Informe uma opção: "))

    @staticmethod
    def main():
        op = 0
        while op != 5:
            op = UI.menu()
            if op == 1: UI.avaliacao_inserir()
            if op == 2: UI.avaliacao_listar()
            if op == 3: UI.atualizar_avaliacao()
            if op == 4: UI.excluir_avaliacao()
    
    @staticmethod
    def avaliacao_inserir():
        id = int(input("Digite o id: "))
        disci = input("Digite a disciplina: ")
        local = input("Digite o local: ")
        t = input("Informe a data de aplicação da avaliação(dd/mm/aaaa): ")
        data = datetime.datetime.strptime(t,"%d/%m/%Y")
        a = Avaliacao(id, disci, local, data)
        Avaliacoes.inserir(a)
    
    @staticmethod
    def avaliacao_listar():
        for a in Avaliacoes.listar():
            print(a)
    
    @staticmethod
    def atualizar_avaliacao():
        UI.avaliacao_listar()
        id = int(input("Digite o id da avaliação a ser atualizada: "))
        disci = input("Digite a disciplina: ")
        local = input("Digite o local: ")
        t = input("Informe a data de aplicação da avaliação(dd/mm/aaaa): ")
        data = datetime.datetime.strptime(t,"%d/%m/%Y")
        a = Avaliacao(id, disci, local, data)

        Avaliacoes.atualizar(a)

    def excluir_avaliacao():
        UI.paciente_listar()
        id = int(input("Informe o id da avaliação a ser excluido: "))
        a = Avaliacao(id,"","","")
        Avaliacoes.excluir(a)

UI.main()