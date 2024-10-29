import streamlit as st
from view import *
from classes import *
import pandas as pd
from user_interface import *

class IndexUI:
    @staticmethod
    def main():
        menu = st.sidebar.selectbox("menu",["Clientes", "Horarios", "Serviços"])
        if menu == "Clientes":
            ClienteUI.main()
        
        if menu == "Horarios":
            HorarioUI.main()

        if menu == "Serviços":
            ServicoUI.main()


IndexUI.main()
