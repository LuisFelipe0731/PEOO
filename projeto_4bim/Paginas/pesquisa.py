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
            if len(objs) == 0: 
                st.write("Nenhum livro cadastrado")
            
            else:    
                dic = []
                for obj in objs: 
                    if obj.titulo == pesq or obj.autor == pesq:
                        dic.append(obj.__dict__)
                df = pd.DataFrame(dic)
                st.dataframe(df)
        
