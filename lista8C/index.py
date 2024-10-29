import streamlit as st
from view import *
from classes import *
import pandas as pd
from user_interface import *

class IndexUI:
    @staticmethod
    def main():
        menu = st.sidebar.selectbox("selecione uma opção:",(ClienteUI.main(), HorarioUI.main(),ServicoUI.main()))
        return menu

IndexUI.main()
