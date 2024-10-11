import streamlit as st
from retangulo import Retangulo

class RetanguloUI:
    def main():
        st.header("Calculos com retangulo")
        b = st.text_input("Digite a base: ")
        h = st.text_input("Digite a altura: ")
        if st.button("Calcular"):
            r = Retangulo(float(b),float(h))
            st.write(r)
            st.write(f"Área = {r.calc_area()}")
            st.write(f"Diagonal = {r.calc_diagonal()}")




