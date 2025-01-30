import pandas as pd
import streamlit as st

px = [0,1,2,3]
py = [10,5,15,10]
dic = {"x": px, "y": py}
chart_data = pd.DataFrame(dic)
st.line_chart(chart_data, x = "x", y = "y")