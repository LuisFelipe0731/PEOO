import json
import datetime
# Clientes, serviços e horarios

class Cliente:
    def __init__(self, nome, id, fone, email):
        self.id = id
        self.nome = nome
        self.fone = fone
        self.email = email   
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.fone} - {self.email}"
        

class Horario:
    def __init__(self,id,data,comfirmado):
        self.id = id
        self.data = data
        self.comfirmado = comfirmado

    def __str__(self):
        return f"{self.id} - {self.data.strftime("%d/%m %H:%M")} - {self.comfirmado}"
        
class Servico:
    def __init__(self,id,descricao,valor,tempo):
        self.id = id
        self.desc = descricao
        self.valor = valor
        self.t = tempo
    def __str__(self):
        return f"{self.id} - {self.desc} - {self.valor} - {self.t.strftime("%H:%M")}"
       

#listas de Objetos
class Clientes:
    objetos = []  
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0                     
        for c in cls.objetos:     
            if c.id > m: m = c.id   
        obj.id = m + 1  
        cls.objetos.append(obj)
        cls.salvar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for c in cls.objetos:
            if c.id == id: return c
        return None 
    
    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            c.nome = obj.nome
            c.email = obj.email
            c.fone = obj.fone
        cls.salvar()   
    
    @classmethod
    def excluir(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None: 
            cls.objetos.remove(c)
        cls.salvar()   
    
    @classmethod
    def salvar(cls):  
        with open("clientes.json", mode = "w") as arquivo:   
            json.dump(cls.objetos, arquivo, default = vars) 
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try: 
            with open("clientes.json", mode = "r") as arquivo:  
                texto = json.load(arquivo)
                for obj in texto:
                    c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])                    
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass

class Horarios:
    horarios = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        n = 0                     
        for h in cls.horarios:     
            if h.id > n:
                n = h.id   
        obj.id = n + 1  
        cls.horarios.append(obj)
        cls.salvar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.horarios
   
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for h in cls.horarios:
            if h.id == id: return h
        return None

    @classmethod
    def atualizar(cls, obj):
        h = cls.listar_id(obj.id)
        if h != None:
            h.data = obj.data
            h.comfirmado = obj.comfirmado
          
        cls.salvar()
    
    @classmethod
    def excluir(cls, obj):
        h = cls.listar_id(obj.id)
        if h != None: 
            cls.horarios.remove(h)
        cls.salvar()
        
    @classmethod
    def salvar(cls):  
        with open("Horarios.json", mode = "w") as arquivo2:  
            json.dump(cls.horarios, arquivo2, default = vars) 
    
    @classmethod
    def abrir(cls):
        cls.horarios = []
        try: 
            with open("Horarios.json", mode = "r") as arquivo2:   
                texto1 = json.load(arquivo2)
                for obj in texto1:
                    h = Horario(obj["id"], obj["data"], obj["comfirmado"])                    
                    cls.horarios.append(h)
        except FileNotFoundError:
            pass
    
class Servicos:
    serv = []
   
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        x = 0                     
        for s in cls.serv:     
            if s.id > x:
                x = s.id   
        obj.id = x + 1  
        cls.serv.append(obj)
        cls.salvar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.serv
   
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for s in cls.serv:
            if s.id == id: return s
        return None

    @classmethod
    def atualizar(cls, obj):
        s = cls.listar_id(obj.id)
        if s != None:
            s.descricao = obj.descricao
            s.valor = obj.valor
            s.tempo = obj.tempo
          
        cls.salvar()
    
    @classmethod
    def excluir(cls, obj):
        s = cls.listar_id(obj.id)
        if s != None: 
            cls.serv.remove(s)
        cls.salvar()
        
    @classmethod
    def salvar(cls):  
            with open("Serviços.json", mode = "w") as arquivo3:  
                json.dump(cls.serv, arquivo3, default = vars) 
    
    @classmethod
    def abrir(cls):
            cls.serv = []
            try: 
                with open("Serviços.json", mode = "r") as arquivo3:   
                    texto2 = json.load(arquivo3)
                    for obj in texto2:
                        s = Servico.obj(["id"], obj["descricao"], obj["valor"], obj["tempo"])                    
                        cls.serv.append(s)
            except FileNotFoundError:
                pass

class UI:
    #Menu
    @staticmethod
    def menu():
        print("1 - Inserir cliente, 2 - listar clientes, 3 - atualizar cliente, 4 - excluir cliente")
        print("5 - Inserir Horario, 6 - Listar Horarios, 7 - Atualizar Horario, 8 - excluir horario")
        print("9 - Inserir serviço, 10 listar serviços, 11 - atualizar seerviço,12 - excluir serviço, 13 - fim")

        return int(input("Informe uma opção: "))
    #Main
    @staticmethod
    def main():
        op = 0
        while op != 13: 
            op = UI.menu()
            #Clientes - funçoes
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()
            #Horarios - funçoes
            if op == 5: UI.horario_inserir()
            if op == 6: UI.horario_listar()
            if op == 7: UI.horario_atualizar()
            if op == 8: UI.horario_excluir()
            #Serviços - funçoes
            if op == 9: UI.servico_inserir()
            if op == 10: UI.servico_listar()
            if op == 11: UI.servico_atualizar()
            if op == 12: UI.servico_excluir()
    
    #Clientes
    @staticmethod
    def cliente_inserir():
        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        c = Cliente(id, nome, email, fone)
        Clientes.inserir(c)

    @staticmethod
    def cliente_listar():
        for c in Clientes.listar():
            print(c)

    @staticmethod
    def cliente_atualizar():
        UI.cliente_listar()
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo fone: ")
        c = Cliente(id, nome, email, fone)
        Horarios.atualizar(c)

    @staticmethod
    def cliente_excluir():
        UI.cliente_listar()
        id = int(input("Informe o id do cliente a ser excluído: "))
        c = Cliente(id, "", "", "")
        Clientes.excluir(c)
    
    #Horarios
    @staticmethod
    def horario_inserir():
        id = int(input("Informe o id: "))
        data1 = input("Informe o horario do serviço (dd/mm hh:mm): ")
        data2 = datetime.datetime.strptime(data1, "%d/%m %H:%M")
        comfirmacao = input("Comfirmaçao: ")
        
        h = Horario(id, data2, comfirmacao)
        Horarios.inserir(h)

    @staticmethod
    def horario_listar():
        for h in Horarios.listar():
            print(h)

    @staticmethod
    def horario_atualizar():
        UI.horario_listar()
        id = int(input("Informe o id do cliente a ser atualizado: "))
        data3 = input("Informe o novo horario(dd/mm hh:mm): ")
        data4 = datetime.datetime.strptime(data3,"%d/%m %H:%M")
        comfirm = input("Informe a nova comfirmação: ")

        h = Horario(id,data4,comfirm)
        Horarios.atualizar(h)

    @staticmethod
    def horario_excluir():
        UI.horario_listar()
        id = int(input("Informe o id do horario a ser excluído: "))
        h = Horario(id, "", "")
        Clientes.excluir(h)
    
    #Serviços
    @staticmethod
    def servico_inserir():
        id = int(input("Informe o id: "))
        desc = input("Insira uma descrição para o serviço: ")
        valor = float(input("Insira o valor: "))
        tempo1 = input("Insira o tempo de duração(hh:mm):")
        tempo2 = datetime.datetime.strptime(tempo1, "%H:%M")
     

        
        s = Servico(id, desc, valor, tempo2)
        Servicos.inserir(s)

    @staticmethod
    def servico_listar():
        for s in Servicos.listar():
            print(s)

    @staticmethod
    def servico_atualizar():
        UI.servico_listar()
        id = int(input("Informe o id do serviço a ser atualizado: "))
        desc = input("Nova descrição: ")
        valor = float(input("Novo valor: "))
        t1 = input("Nova duração(hh:mm): ")
        t2 = datetime.datetime.strptime(t1,"%H:%M")
        s = Servico(id,desc,valor,t2)
        Servicos.atualizar(s)

    @staticmethod
    def servico_excluir():
        UI.servico_listar()
        id = int(input("Informe o id do servico a ser excluído: "))
        s = Servico(id, "", "","")
        Servicos.excluir(s)

UI.main() 