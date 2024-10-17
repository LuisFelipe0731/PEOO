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
            raizes = []
            
            st.write(x)
            st.write(x.Delta())
            x1 = x.raiz1()
            x2 = x.raiz2()

            raizes.append(x1)
            raizes.append(x2)

            st.write(raizes)
           
            #grafico
            xmin = 0
            xmax = 30
            n = 100
            d = (xmax - xmin)/n
            
            px = []
            py = []
            l = xmin
            #while
            while l < xmax:
                y = l**2 - 5*l + 6
                px.append(l)
                py.append(y)
                l = l + d
            l = xmax
            y = l**2 - 5*l + 6
            px.append(l)
            py.append(y)


            
            #desenhar o grafico na tela
            dic = {"x": px, "y": py}
            c_data = pd.DataFrame(dic)
            st.line_chart(c_data, x="x",y="y")


EquacaoUI.main()

