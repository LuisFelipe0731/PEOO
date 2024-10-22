import streamlit as st
from view import *
from cliente import *
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
    def inserir_cliente():
        nome = st.text_input("Informe o nome: ")
        email = st.text_input("Informe o email: ")
        fone = st.text_input("Informe o telefone: ")
        if st.button("Inserir"):
            clientes_inserir(nome, email, fone)
    
    @staticmethod
    def listar_clientes():
        for c in listar_clientes():
            df = pd.DataFrame(
                {
                    "id": [c.id],
                    "nome": [c.nome],
                    "email": [c.email],
                    "fone":[c.fone]
                }
            )
            st.dataframe(
                df,
                column_config= {
                    "id": "_id",
                    "nome": "_nome",
                    "email": "_email",
                    "fone": "_fone"
                }
            )
    
    @staticmethod
    def atualizar_cliente():
        lista_vazia = []
        for c in listar_clientes():
            lista_vazia.append(c)
            
        op = st.selectbox("Selecione um cliente para ser atualizado",(lista_vazia))
        
        st.write(op)
    
        nome = st.text_input("Informe o novo nome: ")
        email = st.text_input("Informe o novo email: ")
        fone = st.text_input("Informe o novo telefone: ")
        
        if st.button("Atualizar"):
            clientes_atualizar(id, nome, email, fone)

        
    
    @staticmethod
    def excluir_cliente():
        lista_vazia = []
        for c in listar_clientes():
            lista_vazia.append(c)
            
        op = st.selectbox("Selecione um cliente para ser excluido",(lista_vazia))

        st.write(op)

        if st.button("Excluir"):
            clientes_excluir(id)
        
        
IndexUI.main()