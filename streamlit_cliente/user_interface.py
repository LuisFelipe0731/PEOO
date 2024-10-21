import streamlit as st
from view import *
from cliente import *

class IndexUI:
    @staticmethod
    def main():
        ClienteUI.main()

        with listar:

        with inserir:
            ClienteUI.inserir_cliente()
            
                
        
        with atualizar:
        
        with excluir:

class ClienteUI:
    @staticmethod
    def main():
        st.header("Cadastro de clientes")
        listar, inserir, atualizar, excluir = st.tabs(["Listar","Inserir","Atualizar","Excluir"])

    @staticmethod
    def inserir_cliente():
        nome = st.text_input("Informe o nome: ")
        email = st.text_input("Informe o email: ")
        fone = st.text_input("Informe o telefone: ")
        clientes_inserir(nome, email, fone)

indexUI.main()