import streamlit as st
from view import *
from classes import *
import pandas as pd

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
    @staticmethod
    def listar_clientes():
        lista = listar_clientes()
        if len(lista) == 0:
            st.write("Nenhum cliente foi adicionado ainda.")
        
        else:
            dic = []
            for c in lista:
                dic.append(c.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)
    
    def inserir_cliente():
        nome = st.text_input("Informe o nome: ")
        email = st.text_input("Informe o email: ")
        fone = st.text_input("Informe o telefone: ")
        if st.button("Inserir"):
            clientes_inserir(nome, email, fone)
            st.rerun()
    
    @staticmethod
    def atualizar_cliente():
        lista = listar_clientes()
        if len(lista) == 0:
            st.write("Nenhum cliente foi adicionado ainda.")
        
        else:
            op = st.selectbox("atualização de clientes", lista)
            nome = st.text_input("Informe o novo nome: ", op.nome)
            email = st.text_input("Informe o novo email: ", op.email)
            fone = st.text_input("Informe o novo telefone: ", op.fone)
            
            if st.button("Atualizar"):
                clientes_atualizar(op.id ,nome, email, fone)
                st.rerun()

        
    
    @staticmethod
    def excluir_cliente():
        lista = listar_clientes()
        if len(lista) == 0:
            st.write("Nenhum cliente foi adicionado ainda.")
        
        else:
            op = st.selectbox("exclusão de clientes", lista)
            if st.button("Excluir"):
                clientes_excluir(op.id)
                st.rerun()

        
        
        
IndexUI.main()