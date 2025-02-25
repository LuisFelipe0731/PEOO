import streamlit as st
from view import View
import time

class AtualizarUI():
    def main():
        st.header("Editar Perfil")
        tab1, tab2 = st.tabs(["Atualizar", "Excluir"])
        with tab1: AtualizarUI.atualizar()
        with tab2: AtualizarUI.excluir()

    def atualizar():
        objs = View.Usuario_listar_id()
        if len(objs) == 0: 
            st.write("Nenhum usuario cadastrado")
        else:
            op = st.selectbox("atulização de usuario", objs)
            nome = st.text_input("Informe o novo nome: ", op.__nome)
            email = st.text_input("Informe o novo e-mail: ", op.__email)
            senha = st.text_input("Informe a nova senha: ", op.__senha ,type="password")
            if st.button("Atualizar"):
                View.Usuario_atualizar(op.__id, nome, email, senha)
                st.success("Conta atualizada com sucesso")
                time.sleep(2)
                st.rerun()
    
    def excluir():
        objs = View.Usuario_listar_id()
        if len(objs) == 0: 
            st.write("Nenhum usuario cadastrado")
        else:
            op = st.selectbox("Exclusão de usuario", objs)
            if st.button("Excluir"):
                View.Livro_excluir(op.__id)
                st.success("Conta excluído com sucesso")
                time.sleep(2)
                st.rerun()
