import streamlit as st
from view import View


class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Entrar"):
            c = View.Usuario_autenticar(email, senha)
            try:
                if c == None: st.write("E-mail ou senha inválidos")
                
                if c != None:
                    st.session_state["usuario_id"] = c['id']
                    st.session_state["usuario_nome"] = c['nome']
                    st.rerun()
            except TypeError:
                return f"invalido invalido"