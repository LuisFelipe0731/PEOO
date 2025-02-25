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
        nome = st.text_input("Informe o novo nome: ", op.__nome)
        email = st.text_input("Informe o novo e-mail: ", op.__email)
        senha = st.text_input("Informe a nova senha: ", op.__senha ,type="password")
        if st.button("Atualizar"):
            View.Usuario_atualizar(op.__id, nome, email, senha)
            st.success("Conta criada com sucesso")
            time.sleep(2)
            st.rerun()
    
    def excluir():
        objs = View.Livro_listar()
        if len(objs) == 0: 
            st.write("Nenhum livro cadastrado")
        else:
            op = st.selectbox("Exclusão de livros", objs)
            if st.button("Excluir"):
                View.Livro_excluir(op.__id)
                st.success("Livro excluído com sucesso")
                time.sleep(2)
                st.rerun()
