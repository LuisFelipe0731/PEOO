import streamlit as st
from view import View

class PesquisarUI:
    def main():
        st.header("Pesquisar: ")
        PesquisarUI.pesquisa()

    def pesquisa():
        pesq = st.text_input("Procurar livro: ")
        