import streamlit as st
import pandas as pd
from view import View
import time

class ManterGeneroUI:
    def main():
        st.header("Cadastro de Livros")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterGeneroUI.listar()
        with tab2: ManterGeneroUI.inserir()
        with tab3: ManterGeneroUI.atualizar()
        with tab4: ManterGeneroUI.excluir()
    
    def listar():
        objs = View.Genero_listar()
        if len(objs) == 0: 
            st.write("Nenhum genero cadastrado")
        else:    
            
            dic = []
            for obj in objs: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)
    #inserir
    def inserir():
        n = st.text_input("Informe o nome do genêro: ")
        d = st.text_input("Informe uma descrição: ")
        
        if st.button("Inserir"):
            View.Genero_inserir(n,d)
            st.success("Genêro inserido com sucesso")
            time.sleep(2)
            st.rerun()
    
    #atualizar
    def atualizar():
        objs = View.Genero_listar()
        if len(objs) == 0: 
            st.write("Nenhum genêro cadastrado")
        else:
            op = st.selectbox("Atualização de genêros", objs)
            n = st.text_input("Informe o novo nome: ", op.__titulo)
            d = st.text_input("Informe a nova descrição: ", op.__autor)
    
            
            if st.button("Atualizar"):
                View.Genero_atualizar(op.__id, n, d)
                st.success("Genêro atualizado com sucesso")
                time.sleep(2)
                st.rerun()
    
    def excluir():
        objs = View.Genero_listar()
        if len(objs) == 0: 
            st.write("Nenhum livro cadastrado")
        else:
            op = st.selectbox("Exclusão de Genêros", objs)
            if st.button("Excluir"):
                View.Genero_excluir(op.__id)
                st.success("Genêro excluído com sucesso")
                time.sleep(2)
                st.rerun()