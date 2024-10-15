from equacao2grau import Equacao2grau
import streamlit as st
import pandas as pd

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
            
            st.write(f" raiz 1: {x.raiz1()}")
            st.write(f"raiz 2: {x.raiz2()}")
            #grafico
            xmin = 0
            xmax = 
            n = 100
            d = (xman - xmin)/n
            px = []
            py = []
            while l = xmax
            #desenhar o grafico na tela
            dic = {"x": px, "y": py}
            c_data = pd.DataFrame(dic)
            st.line_chart(c_data, x="x",y="y")


EquacaoUI.main()

