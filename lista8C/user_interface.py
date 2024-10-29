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

class ServicoUI:
    @staticmethod
    def main():
        st.header("Cadastro de serviços")
        listar, inserir, atualizar, excluir = st.tabs(["Listar","Inserir","Atualizar","Excluir"])

        with listar:
            ServicoUI.listar_servicos()

        with inserir:
            ServicoUI.inserir_servico()
             
        with atualizar:
            ServicoUI.atualizar_servico()
        
        with excluir:
            ServicoUI.excluir_servico()

    @staticmethod
    def listar_servicos():
        lista = View_servico.listar_servicos()
        if len(lista) == 0:
            st.write("Nenhum serviço foi adicionado ainda.")
        
        else:
            dic = []
            for c in lista:
                dic.append(c.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)
    
    def inserir_servico():
        desc = st.text_input("Informe a descrição do serviço: ")
        valor = st.text_input("Informe o valor: ")
        tempo = st.text_input("Informe a duração(hh:mm): ")
        if st.button("Inserir"):
            View_servico.servicos_inserir(desc,valor,tempo)
            st.rerun()
    
    @staticmethod
    def atualizar_servico():
        lista = View_servico.listar_servicos()
        if len(lista) == 0:
            st.write("Nenhum serviço foi adicionado ainda.")
        
        else:
            op = st.selectbox("atualização de serviços", lista)
            desc = st.text_input("Informe a descrição do serviço: ",op.desc)
            valor = st.text_input("Informe o valor: ",op.valor)
            tempo = st.text_input("Informe a duração(hh:mm): ",op.t)
            
            if st.button("Atualizar"):
                View_servico.servicos_atualizar(op.id,desc,valor,tempo)
                st.rerun()
    
    @staticmethod
    def excluir_servico():
        lista = View_servico.listar_servicos()
        if len(lista) == 0:
            st.write("Nenhum serviço foi adicionado ainda.")
        
        else:
            op = st.selectbox("atualização de clientes", lista)
            nome = st.text_input("Informe o novo nome: ", op.nome)
            email = st.text_input("Informe o novo email: ", op.email)
            fone = st.text_input("Informe o novo telefone: ", op.fone)
            
            if st.button("Atualizar"):
                View_servico.servicos_excluir()
                st.rerun()


