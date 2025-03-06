import streamlit as st
from view import View
import pandas as pd

class PesquisarUI:
    def main():
        st.header("Pesquisar: ")
        PesquisarUI.pesquisa()

    def pesquisa():
        pesq = st.text_input("Procurar livro: ")
        #Butao de pesquisa:
        if st.button("Pesquisar"):
            objs = View.Livro_listar()

            lista = []
            for obj in objs: 
                if obj.titulo == pesq:
                    lista.append(obj.titulo)
            df = pd.DataFrame(lista)
            st.dataframe(df)
    
