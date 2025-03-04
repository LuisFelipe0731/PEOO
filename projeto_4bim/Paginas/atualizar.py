import streamlit as st
from view import View
import time

class AtualizarUI():
    def main():
        st.header("Editar Perfil")
        AtualizarUI.atualizar()


    #Atualização de Usuario
    def atualizar():
        objs = View.Usuario_listar_id()
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
        op = View.Usuario_listar_id(st.session_state['usuario_id'])

    