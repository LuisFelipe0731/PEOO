import streamlit as st
from view import *
from cliente import *

class IndexUI:
    @staticmethod
    def main():
        st.header("Cadastro de clientes")
        listar, inserir, atualizar, excluir = st.tabs(["Listar","Inserir","Atualizar","Excluir"])

        with listar:

        with inserir:
            
                
        
        with atualizar:
        
        with excluir:

class ClienteUI:
    @staticmethod
    def main():

    @staticmethod
    def inserir_cliente():
        nome = st.text_input("Informe o nome: ")
        email = st.text_input("Informe o email: ")
        fone = st.text_input("Informe o telefone: ")

indexUI.main()