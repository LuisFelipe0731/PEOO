from classes import *

#view - clientes
class View_cliente:
    def clientes_inserir(nome, email, fone):
        Clientes.inserir(Cliente(0,nome,email,fone))

    def listar_clientes():
        return Clientes.listar()

    def clientes_atualizar(id, nome, email, fone):
        c = Cliente(id,nome,email,fone)
        Clientes.atualizar(c)

    def clientes_excluir(id):
        c = Cliente(id,"","","")
        Clientes.excluir(c)

#view - horarios
class View_horario:
    def horarios_inserir(data):
        Horarios.inserir(Horario(0,data))

    def listar_horarios():
        return Horarios.listar()

    def horarios_atualizar(id, data):
        c = Horario(id,data)
        Horarios.atualizar(c)

    def horarios_excluir(id):
        c = Horario(id,"")
        Horarios.excluir(c)

#view - serviços
class View_servico:
    def servicos_inserir(desc, valor, tempo):
        Servicos.inserir(Servico(0,desc,valor,tempo))

    def listar_servicos():
        return Servicos.listar()

    def servicos_atualizar(id, desc,valor,tempo):
        c = Servico(id,desc,valor,tempo)
        Servicos.atualizar(c)

    def servicos_excluir(id):
        c = Servico(id,"","","")
        Servicos.excluir(c)

