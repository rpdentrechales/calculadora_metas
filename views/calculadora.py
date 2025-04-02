import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Calculadora de Metas", page_icon="💎",layout="wide")

st.title("Calculadora de Metas")

porcentagem = st.number_input(label="porcentagem", min_value=0.0, max_value=100.0,label_visibility="hidden")

st.write(porcentagem)