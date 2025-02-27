import streamlit as st
from view import View

class GraficoUI:
    def main():
        st.header("Grafico: ")
        
        data = View.grafico()
        cor = ["#33FF11", "55AA88", "EEEE22", "FF7777","550055"]
        st.bar_chart(data,x="Generos",y="livros",color=cor, stack=False)