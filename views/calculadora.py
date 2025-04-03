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
   meta_rede = {"value":0,
                "dont_use":True}
   st.session_state['meta_rede'] = meta_rede

   
meta_rede_display = imprimir_metric("meta_rede","Meta Rede",grid_1)
rede_popover = imprimir_popover("Meta Rede (R$)","meta_rede", grid_2)

# rede_popover= grid_2.popover("Ajustar")

# meta_rede = rede_popover.number_input(label="Meta Rede (R$)",
#                                       min_value=0.0,
#                                       value=None,
#                                       on_change=atualizar_valores,
#                                       key="meta_rede_value",
#                                       kwargs = {"update_var":"meta_rede",
#                                                 "update_arg":"value",
#                                                 "update_value":"meta_rede_value"})

# meta_rede_nome = rede_popover.toggle(label="Calcular depois",
#                                      value=False,
#                                      on_change=atualizar_valores,
#                                      key="meta_rede_nome",
#                                      kwargs = {"update_var":"meta_rede",
#                                                 "update_arg":"dont_use",
#                                                 "update_value":"meta_rede_nome"})
