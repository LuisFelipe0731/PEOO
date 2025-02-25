import streamlit as st
import pandas as pd
from view import View
import time
from datetime import datetime

class ManterLivroUI:
    def main():
        st.header("Cadastro de Livros")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterLivroUI.listar()
        with tab2: ManterLivroUI.inserir()
        with tab3: ManterLivroUI.atualizar()
        with tab4: ManterLivroUI.excluir()
    
    def listar():
        objs = View.Livro_listar()
        if len(objs) == 0: 
            st.write("Nenhum livro cadastrado")
        else:    
            
            dic = []
            for obj in perfis: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)
    
    def inserir():
        t = st.text_input("Informe o titulo do livro: ")
        a = st.text_input("Informe o autor: ")
        data = st.text_input("Informe a data de publicação: ")
        if st.button("Inserir"):
            View.Livro_inserir(t,a,data)
            st.success("Livro inserido com sucesso")
            time.sleep(2)
            st.rerun()
    
    def atualizar():
        objs = View.Livro_listar()
        if len(objs) == 0: 
            st.write("Nenhum livro cadastrado")
        else:
            op = st.selectbox("Atualização de livros", objs)
            t = st.text_input("Informe o novo titulo: ", op.__titulo)
            a = st.text_input("Informe o novo autor: ", op.__autor)
            data = st.text_input("Informe a nova data de publicação: ", op.__data_publicacao)
            
            if st.button("Atualizar"):
                View.cliente_atualizar(op.__id, t, a, data)
                st.success("Livro atualizado com sucesso")
                time.sleep(2)
                st.rerun()
    
    def excluir():
        objs = View.Livro_listar()
        if len(objs) == 0: 
            st.write("Nenhum livro cadastrado")
        else:
            op = st.selectbox("Exclusão de perfis", objs)
            if st.button("Excluir"):
                View.Livro_excluir(op.__id)
                st.success("Livro excluído com sucesso")
                time.sleep(2)
                st.rerun()