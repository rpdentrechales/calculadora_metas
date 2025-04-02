import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Calculadora de Metas", page_icon="💎",layout="wide")

st.title("Calculadora de Metas")

col_1,col_2,spacer = st.columns([1,1,10])

with col_1:
    
  meta_rede = st.number_input(label="Meta Rede")

st.write(meta_rede)