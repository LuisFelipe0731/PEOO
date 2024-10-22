import streamlit as st
from view import *
from cliente import *

class IndexUI:
    @staticmethod
    def main():
        ClienteUI.main()

        
class ClienteUI:
    @staticmethod
    def main():
        st.header("Cadastro de clientes")
        listar, inserir, atualizar, excluir = st.tabs(["Listar","Inserir","Atualizar","Excluir"])

        with listar:
            ClienteUI.listar_clientes()

        with inserir:
            ClienteUI.inserir_cliente()
             
        with atualizar:
            ClienteUI.atualizar_cliente()
        
        with excluir:
            ClienteUI.excluir_cliente()

    @staticmethod
    def inserir_cliente():
        nome = st.text_input("Informe o nome: ")
        email = st.text_input("Informe o email: ")
        fone = st.text_input("Informe o telefone: ")
        if st.button("Inserir"):
            clientes_inserir(nome, email, fone)
    
    @staticmethod
    def listar_clientes():
        for c in listar_clientes():
            st.dataframe(
                df,
                column_config= {
                    
                }
            )
    
    @staticmethod
    def atualizar_cliente():
    
    @staticmethod
    def excluir_cliente():

indexUI.main()