import streamlit as st
from view import *
from classes import *
import pandas as pd

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
    def listar_clientes():
        lista = View_cliente.listar_clientes()
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
            View_cliente.clientes_inserir(nome, email, fone)
            st.rerun()
    
    @staticmethod
    def atualizar_cliente():
        lista = View_cliente.listar_clientes()
        if len(lista) == 0:
            st.write("Nenhum cliente foi adicionado ainda.")
        
        else:
            op = st.selectbox("atualização de clientes", lista)
            nome = st.text_input("Informe o novo nome: ", op.nome)
            email = st.text_input("Informe o novo email: ", op.email)
            fone = st.text_input("Informe o novo telefone: ", op.fone)
            
            if st.button("Atualizar"):
                View_cliente.clientes_atualizar(op.id ,nome, email, fone)
                st.rerun()

        
    
    @staticmethod
    def excluir_cliente():
        lista = View_cliente.listar_clientes()
        if len(lista) == 0:
            st.write("Nenhum cliente foi adicionado ainda.")
        
        else:
            op = st.selectbox("exclusão de clientes", lista)
            if st.button("Excluir"):
                View_cliente.clientes_excluir(op.id)
                st.rerun()

class HorarioUI:
    @staticmethod
    def main():
        st.header("Cadastro de horarios")
        listar, inserir, atualizar, excluir = st.tabs(["Listar","Inserir","Atualizar","Excluir"])

        with listar:
            HorarioUI.listar_horarios()

        with inserir:
            HorarioUI.inserir_horarios()
             
        with atualizar:
            HorarioUI.atualizar_horarios()
        
        with excluir:
            HorarioUI.excluir_horarios()

    @staticmethod
    def listar_horarios():
        lista = View_horario.listar_horarios()
        if len(lista) == 0:
            st.write("Nenhum horario foi adicionado ainda.")
        
        else:
            dic = []
            for c in lista:
                dic.append(c.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)
    
    def inserir_horarios():
        data = st.text_input("Informe a data(dd/mm hh:mm): ")
        
        if st.button("Inserir"):
            View_horario.horarios_inserir(data)
            st.rerun()
    
    @staticmethod
    def atualizar_horarios():
        lista = View_horario.listar_horarios()
        if len(lista) == 0:
            st.write("Nenhum horario foi adicionado ainda.")
        
        else:
            op = st.selectbox("atualização de horarios", lista)
            data = st.text_input("Informe a nova data(dd/mm hh:mm): ", op.data)

            
            if st.button("Atualizar"):
                View_horario.horarios_atualizar(op.id,data)
                st.rerun()

        
    
    @staticmethod
    def excluir_horarios():
        lista = View_horario.listar_horarios()
        if len(lista) == 0:
            st.write("Nenhum horario foi adicionado ainda.")
        
        else:
            op = st.selectbox("exclusão de horarios", lista)
            if st.button("Excluir"):
                View_horario.horarios_excluir(op.id)
                st.rerun()
