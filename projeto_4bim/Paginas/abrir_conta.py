import streamlit as st
from view import View
import time

class AbrirContaUI:
    def main():
        st.header("Abrir Conta no Sistema")
        AbrirContaUI.inserir()

    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Inserir"):
            View.Usuario_inserir(nome, email, senha)
            st.success("Conta criada com sucesso")
            time.sleep(2)
            st.rerun()