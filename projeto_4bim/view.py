from Models.crud import CRUD
from Models.livro import Livro, Livros
from Models.usuario import Usuario,Usuarios
from Models.genero import Genero, Generos
from Models.exemplar import Exemplar, Exemplares
from Models.compra import Compra, Compras

#View
class View:
    #Usuario - Admin
    def Usuario_inserir(nome, email, senha):
        c = Usuario(0, nome, email, senha)
        Usuarios.inserir(c)

    def Usuario_listar():
        return Usuarios.listar()    

    def Usuario_listar_id(id):
        return Usuarios.listar_id(id)    

    def Usuario_atualizar(id,nome, email, senha):
        c = Usuario(id, nome, email, senha)
        Usuarios.atualizar(c)

    def Usuario_excluir(id):
        c = Usuario(id, "", "", "")
        Usuarios.excluir(c)
    
    def Usuario_admin():
        for c in View.Usuario_listar():
            if c.email == "admin": return
        View.Usuario_inserir("admin","admin","1234")
    
    def Usuario_autenticar(email, senha):
        for c in View.Usuario_listar():
            if c.__email == email and c.__senha == senha:
                return {"id" : c.__id ,"nome" : c.__nome }
        return None
    
    #Livros
    def Livro_inserir(titulo, autor, data, genero):
        c = Livro(0, titulo, autor, data)
        c.__id_genero = genero
        Livros.inserir(c)

    def Livro_listar():
        return Livros.listar()    

    def Livro_listar_id(id):
        return Livros.listar_id(id)    

    def Livro_atualizar(id,titulo, autor, data, genero):
        c = Livro(id, titulo, autor, data)
        c.__id_genero = genero
        Livros.atualizar(c)

    def Livro_excluir(id):
        c = Livro(id, "", "", "")
        Livros.excluir(c) 

    def Pesquisar_livro(nome):
        for c in View.Livro_listar():
            if c.__nome == nome:
                return c
   
    #Generos
    def Genero_inserir(nome, desc):
        c = Genero(0, nome, desc)
        Generos.inserir(c)

    def Genero_listar():
        return Generos.listar()   
    
    def Genero_listar_id():
        return Generos.listar_id()    

    def Genero_atualizar(id, nome, desc):
        c = Genero(id, nome, desc)
        Generos.atualizar(c)

    def Genero_excluir(id):
        c = Genero(id, "", "")
        Generos.excluir(c)    

    #Exemplares
    def Exemplar_inserir(edicao, valor, livro):
        c = Exemplar(0, edicao, valor)
        c.__id_livro = livro
        Exemplares.inserir(c)

    def Exemplar_listar():
        return Exemplares.listar()    

    def Exemplar_listar_id(id):
        return Exemplares.listar_id(id)    

    def Exemplar_atualizar(id, edicao, valor, livro):
        c = Exemplar(id, edicao, valor)
        c.__id_livro = livro
        Exemplares.atualizar(c)

    def Exemplar_excluir(id):
        c = Exemplar(id, "")
        Exemplares.excluir(c)    
    
    #Compras
    def Compra_inserir(usuario):
        c = Compra(0)
        c.__id_user = usuario
        Compras.inserir(c)

    def Compra_listar():
        return Compras.listar()    

    def Compra_listar_id(id):
        return Compras.listar_id(id)    

    def Compra_atualizar(id,usuario):
        c = Compra(id)
        c.__id_user = usuario
        Compras.atualizar(c)

    def Compra_excluir(id):
        c = Compra(id)
        Compras.excluir(c)