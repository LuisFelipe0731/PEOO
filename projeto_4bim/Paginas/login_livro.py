import streamlit as st
from view import View


class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        
        if st.button("Entrar"):
            c = View.Usuario_autenticar(email, senha)
            if c == None:
                st.write("E-mail ou senha inválidos")
                
            if c != None:
                st.session_state['usuario_id'] = c[1]
                st.session_state['usuario_nome'] = c[2]

                st.rerun()
            