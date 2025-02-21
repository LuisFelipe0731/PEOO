from Paginas.livrosUI import ManterLivroUI
from Paginas.generosUI import ManterGeneroUI
from Paginas.exemplaresUI import ManterExemplarUI
from Paginas.comprasUI import ManterCompraUI
from Paginas.usuariosUI import ManterUsuarioUI
from Paginas.grafico import GraficoUI
from Paginas.comprar import ComprarUI
from Paginas.login_livro import LoginUI
from Paginas.abrir_conta import AbrirContaUI
from Paginas.pesquisa import PesquisarUI
from view import View

import streamlit as st

class IndexUI:
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()
               
    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Livros", "Cadastro de Generos", "Cadastro de Exemplares","Cadastro de Compras", "Graficos"])
        if op == "Cadastro de Livros": ManterLivroUI.main()
        if op == "Cadastro de Generos": ManterGeneroUI.main()
        if op == "Cadastro de Exemplares": ManterExemplarUI.main()
        if op == "Cadastro de Compras": ManterCompraUI.main()
        if op == "Graficos": GraficoUI.main()

    def menu_usuario():
        op = st.sidebar.selectbox("Menu", ["Pesquisar", "Comprar","Graficos","Conta"])
        if op == "Graficos": GraficoUI.main()
        if op == "Comprar": ComprarUI.main()
        if op == "Pesquisar": PesquisarUI.main()
        if op == "Conta": ManterUsuarioUI.main()


    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()
    
    def sidebar():
        if "cliente_id" not in st.session_state:
            # usuário não está logado
            IndexUI.menu_visitante()   
        else:
            # usuário está logado, verifica se é o admin
            admin = st.session_state["usuario_nome"] == "admin"
            # mensagen de bem-vindo
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            # menu do usuário
            if admin: IndexUI.menu_admin()
            else: IndexUI.menu_cliente()
            # controle de sair do sistema
            IndexUI.sair_do_sistema() 
    
    def main():
        View.Usuario_admin()
       
        IndexUI.sidebar()
       
IndexUI.main()