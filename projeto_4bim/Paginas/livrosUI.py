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
            for obj in objs: 
                #id do genero
                genero = View.Genero_listar_id(obj.__id__genero)
                if genero != None: genero = genero.__nome
                
                dic.append({"id":obj.__id, "titulo": obj.__titulo, "autor": obj.__autor, "data": obj.__data_publicacao, "genero": genero})
            
            df = pd.DataFrame(dic)
            st.dataframe(df)
    
    def inserir():
        generos = View.Genero_listar()
        t = st.text_input("Informe o titulo do livro: ")
        a = st.text_input("Informe o autor: ")
        data = st.text_input("Informe a data de publicação (formato: dd/mm/aa): ", datetime.now().strftime("%d/%m/%Y"))
        genero = st.selectbox("Informe o perfil: ", generos, index = None)
        
        if st.button("Inserir"):
            id_genero = None
            if id_genero != None: id_genero = genero.__id
            
            View.Livro_inserir(t,a,datetime.strptime(data, "%d/%m/%Y"),id_genero)
            st.success("Livro inserido com sucesso")
            time.sleep(2)
            st.rerun()
    
    def atualizar():
        objs = View.Livro_listar()
        if len(objs) == 0: 
            st.write("Nenhum livro cadastrado")
        else:
            generos = View.Genero_listar()
            op = st.selectbox("Atualização de livros", objs)
            t = st.text_input("Informe o novo titulo: ", op.__titulo)
            a = st.text_input("Informe o novo autor: ", op.__autor)
            data = st.text_input("Informe a nova data de publicação (formato: dd/mm/aa): ", op.__data_publicacao.strftime("%d/%m/%Y"))
            id_genero = None if op.id_genero in [0, None] else op.id_genero
            genero = st.selectbox("Informe o novo genero", generos, next((i for i, c in enumerate(generos) if c.__id == id_genero), None))
            
            if st.button("Atualizar"):
                id_genero = None
                if id_genero != None: id_genero = genero.__id
                View.Livro_atualizar(op.__id, t, a, datetime.strptime(data, "%d/%m/%Y"),id_genero)
                st.success("Livro atualizado com sucesso")
                time.sleep(2)
                st.rerun()
    
    def excluir():
        objs = View.Livro_listar()
        if len(objs) == 0: 
            st.write("Nenhum livro cadastrado")
        else:
            op = st.selectbox("Exclusão de livros", objs)
            if st.button("Excluir"):
                View.Livro_excluir(op.__id)
                st.success("Livro excluído com sucesso")
                time.sleep(2)
                st.rerun()