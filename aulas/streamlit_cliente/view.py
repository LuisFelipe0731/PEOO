from cliente import *

#funcoes view
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