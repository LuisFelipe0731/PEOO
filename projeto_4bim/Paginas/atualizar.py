import streamlit as st
from view import View
import time

class AtualizarUI():
    def main():
        st.header("Editar Perfil")
        op = st.sidebar.selectbox("Menu", ["Atulizar Conta", "Excluir Conta"])
        if op == "Atulizar Conta": AtualizarUI.atualizar()
        if op == "Excluir Conta": AtualizarUI.excluir()


    #Atualização de Usuario
    def atualizar():
        objs = View.Usuario_listar()
        if len(objs) == 0: 
            st.write("Nenhum usuario cadastrado")
        else:
            op = View.Usuario_listar_id(st.session_state['usuario_id'])
            nome = st.text_input("Informe o novo nome: ", op.nome)
            email = st.text_input("Informe o novo e-mail: ", op.email)
            senha = st.text_input("Informe a nova senha: ", op.senha ,type="password")
            if st.button("Atualizar"):
                View.Usuario_atualizar(op.id, nome, email, senha)
                st.success("Conta atualizada com sucesso")
                time.sleep(2)
                st.rerun()
    
    def excluir():
        objs = View.Usuario_listar()
        if len(objs) == 0: 
            st.write("Nenhum usuario cadastrado")
        else:
            op = View.Usuario_listar_id(st.session_state['usuario_id'])
            st.write("Excluir conta? ")
            if st.button("Confirmar"):
                View.Usuario_excluir(op.id)
                st.success("Conta excluida com sucesso")
                time.sleep(2)
                st.rerun()

    