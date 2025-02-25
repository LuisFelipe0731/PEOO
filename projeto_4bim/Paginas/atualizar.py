import streamlit as st
from view import View

class AtualizarUI():
    def main():
        st.header("Editar Perfil")
        tab1, tab2 = st.tabs(["Atualizar", "Excluir"])
        with tab1: AtualizarUI.atualizar()
        with tab2: AtualizarUI.excluir()
