import streamlit as st
import pandas as pd
from view import View
import time

class ManterLivroUI:
    def main():
        st.header("Cadastro de Livros")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterLivroUI.listar()
        with tab2: ManterLivroUI.inserir()
        with tab3: ManterLivroUI.atualizar()
        with tab4: ManterLivroUI.excluir()
    
    def listar():
        perfis = View.Livro_listar()
        if len(perfis) == 0: 
            st.write("Nenhum livro cadastrado")
        else:    
            
            dic = []
            for obj in perfis: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)
    
    def inserir():
        nome = st.text_input("Informe o titulo do livro: ")
        desc = st.text_input("Informe a descrição: ")
        beneficio = st.text_input("Informe o beneficio: ")
        if st.button("Inserir"):
            View.perfil_inserir(nome,desc,beneficio)
            st.success("Perfil inserido com sucesso")
            time.sleep(2)
            st.rerun()
    
    def atualizar():
        perfis = View.perfil_listar()
        if len(perfis) == 0: 
            st.write("Nenhum perfil cadastrado")
        else:
            op = st.selectbox("Atualização de perfis", perfis)
            nome = st.text_input("Informe o novo nome do perfil: ", op.nome)
            desc = st.text_input("Informe a nova descrição: ", op.desc)
            beneficio = st.text_input("Informe o novo beneficio: ", op.beneficio)
            
            if st.button("Atualizar"):
                View.cliente_atualizar(op.id, nome, desc, beneficio)
                st.success("perfil atualizado com sucesso")
                time.sleep(2)
                st.rerun()
    
    def excluir():
        perfis = View.perfil_listar()
        if len(perfis) == 0: 
            st.write("Nenhum perfil cadastrado")
        else:
            op = st.selectbox("Exclusão de perfis", perfis)
            if st.button("Excluir"):
                View.perfil_excluir(op.id)
                st.success("perfil excluído com sucesso")
                time.sleep(2)
                st.rerun()