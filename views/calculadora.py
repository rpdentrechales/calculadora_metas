import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Calculadora de Metas", page_icon="💎",layout="wide")

st.title("Calculadora de Metas")

col_1,col_2,spacer = st.columns([1,1,5],gap="small",vertical_alignment="center")

if 'meta_rede' in st.session_state:
    
    meta_rede = st.session_state['meta_rede']

else:
   meta_rede = 0

   
meta_rede_display = col_1.metric(label="Meta Rede",value=meta_rede)
rede_popover= col_2.popover("Ajustar")
meta_rede = rede_popover.number_input(label="Meta Rede (R$)",min_value=0.0)