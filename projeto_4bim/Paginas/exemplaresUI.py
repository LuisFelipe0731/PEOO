import streamlit as st
import pandas as pd
from view import View
import time

class ManterExemplarUI:
    def main():
        st.header("Cadastro de Exemplares")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterExemplarUI.listar()
        with tab2: ManterExemplarUI.inserir()
        with tab3: ManterExemplarUI.atualizar()
        with tab4: ManterExemplarUI.excluir()
    
    def listar():
        objs = View.Exemplar_listar()
        if len(objs) == 0: 
            st.write("Nenhum exemplar cadastrado")
        else:    
            
            dic = []
            for obj in objs: 
                #id do livro
                livro = View.Livro_listar_id(obj.__id_livro)
                if livro != None: livro = livro.__titulo
                
                dic.append({"id":obj.__id, "edição": obj.__ed, "valor": obj.__valor, "livro": livro})
            
            df = pd.DataFrame(dic)
            st.dataframe(df)
    
    def inserir():
        livros = View.Livro_listar()
        e = st.text_input("Informe a edição do exemplar: ")
        v = st.text_input("Informe o valor do exemplar: ")
        livro = st.selectbox("Informe o livro: ", livros, index = None)
        
        if st.button("Inserir"):
            id_livro = None
            if id_livro != None: id_livro = livro.__id
            
            View.Exemplar_inserir(e, float(v), id_livro)
            st.success("Exemplar inserido com sucesso")
            time.sleep(2)
            st.rerun()
    
    def atualizar():
        objs = View.Exemplar_listar()
        if len(objs) == 0: 
            st.write("Nenhum exemplar cadastrado")
        else:
            livros = View.Livro_listar()
            op = st.selectbox("Atualização de exemplares", objs)
            e = st.text_input("Informe a nova edição: ", op.__ed)
            v = st.text_input("Informe o novo valor: ", op.__valor)
            id_livro = None if op.__id_livro in [0, None] else op.__id_livro
            livro = st.selectbox("Informe o novo livro", livros, next((i for i, c in enumerate(livros) if c.__id == id_livro), None))
            
            if st.button("Atualizar"):
                id_livro = None
                if id_livro != None: id_livro = livro.__id
                View.Exemplar_atualizar(op.__id, e, float(v), id_livro)
                st.success("Exemplar atualizado com sucesso")
                time.sleep(2)
                st.rerun()
    
    def excluir():
        objs = View.Exemplar_listar()
        if len(objs) == 0: 
            st.write("Nenhum exemplar cadastrado")
        else:
            op = st.selectbox("Exclusão de exemplares", objs)
            if st.button("Excluir"):
                View.Exemplar_excluir(op.__id)
                st.success("exemplar excluído com sucesso")
                time.sleep(2)
                st.rerun()