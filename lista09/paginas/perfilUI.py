import streamlit as st
import pandas as pd
from views import View
import time

class ManterPerfilUI:
    def main():
        st.header("Cadastro de Perfil")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterPerfilUI.listar()
        with tab2: ManterPerfilUI.inserir()
        with tab3: ManterPerfilUI.atualizar()
        with tab4: ManterPerfilUI.excluir()