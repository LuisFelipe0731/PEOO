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
            objs = View.Pesquisar_livro(pesq)

            dic = []
            for obj in objs: 
                dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)
    
