import streamlit as st
import pandas as pd
import datetime
from auxiliar.aux_display import *

st.set_page_config(page_title="Calculadora de Metas", page_icon="💎",layout="wide")

st.title("Calculadora de Metas")

grid_1,grid_2,spacer = st.columns([1,1,5],gap="small",vertical_alignment="center")

if 'meta_rede' in st.session_state:
    
    meta_rede = st.session_state['meta_rede']

else:
   meta_rede = None

   
meta_rede_display = grid_1.metric(label="Meta Rede",value=meta_rede)
rede_popover= grid_2.popover("Ajustar")

meta_rede = rede_popover.number_input(label="Meta Rede (R$)",min_value=0.0,value=None,on_change=)
meta_rede_nome = rede_popover.toggle(label="deixar em branco",value=False,on_change=test)
