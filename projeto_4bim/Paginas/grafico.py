import streamlit as st
from view import View

class GraficoUI:
    def main():
        st.header("Grafico: ")
        data = View.grafico()
        st.bar_chart(data,x="Generos",y="livros",color=site, stack=False)