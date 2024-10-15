from equacao2grau import Equacao2grau
import streamlit as st

class EquacaoUI:
    def main():
        st.header("Equação do segundo grau: ")
        a = st.text_input("Digite o valor de A: ")
        b = st.text_input("Digite o valor de B: ")
        c = st.text_input("Digite o valor de C: ")
            
        if st.button("calcular"):
            x = Equacao2grau(int(a), int(b), int(c))
            
            st.write(x)
            st.write(x.Delta())
            
            st.write(x.raiz1())
            st.write(x.raiz2())

EquacaoUI.main()

