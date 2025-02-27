from classes.cliente2 import Cliente, Clientes
from classes.horario2 import Horario, Horarios
from classes.servico2 import Servico, Servicos
from classes.perfil import Perfil, Perfis
from datetime import datetime, timedelta

class View:
    #admin
    def cliente_admin():
        for c in View.cliente_listar():
            if c.email == "admin": return
        View.cliente_inserir("admin", "admin", "1234", "1234",0)
    
    #clientes
    def cliente_inserir(nome, email, fone, senha, id_perfil):
        c = Cliente(0, nome, email, fone, senha)
        c.id_perfil = id_perfil
        Clientes.inserir(c)

    def cliente_listar():
        return Clientes.listar()    

    def cliente_listar_id(id):
        return Clientes.listar_id(id)    

    def cliente_atualizar(id, nome, email, fone, senha, id_perfil):
        c = Cliente(id, nome, email, fone, senha)
        c.id_perfil = id_perfil
        Clientes.atualizar(c)

    def cliente_excluir(id):
        c = Cliente(id, "", "", "", "")
        Clientes.excluir(c)    

    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.email == email and c.senha == senha:
                return {"id" : c.id, "nome" : c.nome }
        return None
    
    #horarios
    def horario_inserir(data, confirmado, id_cliente, id_servico):
        c = Horario(0, data)
        c.confirmado = confirmado
        c.id_cliente = id_cliente
        c.id_servico = id_servico
        Horarios.inserir(c)

    def horario_listar():
        return Horarios.listar()    

    def horario_listar_disponiveis():
        horarios = View.horario_listar()
        disponiveis = []
        for h in horarios:
            if h.data >= datetime.now() and h.id_cliente == None: disponiveis.append(h)
        return disponiveis   

    def horario_atualizar(id, data, confirmado, id_cliente, id_servico):
        c = Horario(id, data)
        c.confirmado = confirmado
        c.id_cliente = id_cliente
        c.id_servico = id_servico
        Horarios.atualizar(c)

    def horario_excluir(id):
        c = Horario(id, None)
        Horarios.excluir(c)    

    def horario_abrir_agenda(data, hora_inicio, hora_fim, intervalo):
        i = data + " " + hora_inicio   
        f = data + " " + hora_fim      
        d = timedelta(minutes=intervalo)
        di = datetime.strptime(i, "%d/%m/%Y %H:%M")
        df = datetime.strptime(f, "%d/%m/%Y %H:%M")
        x = di
        while x <= df:
            
            View.horario_inserir(x, False, None, None)

            x = x + d

    #serviços
    def servico_inserir(descricao, valor, duracao):
        c = Servico(0, descricao, valor, duracao)
        Servicos.inserir(c)

    def servico_listar():
        return Servicos.listar()    

    def servico_listar_id(id):
        return Servicos.listar_id(id)    

    def servico_atualizar(id, descricao, valor, duracao):
        c = Servico(id, descricao, valor, duracao)
        Servicos.atualizar(c)

    def servico_excluir(id):
        c = Servico(id, "", 0, 0)
        Servicos.excluir(c)    
    
    #perfis
    def perfil_inserir(nome, desc, beneficio):
        c = Perfil(0, nome, desc, beneficio)
        Perfis.inserir(c)

    def perfil_listar():
        return Perfis.listar()    

    def perfil_listar_id(id):
        return Perfis.listar_id(id)    

    def perfil_atualizar(id, nome, desc, beneficio):
        c = Perfil(id, nome, desc, beneficio)
        Perfis.atualizar(c)

    def perfil_excluir(id):
        c = Perfil(id, "", "", "")
        Perfis.excluir(c)    