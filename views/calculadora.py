import streamlit as st
import pandas as pd
import datetime
from auxiliar.aux_display import *

st.set_page_config(page_title="Calculadora de Metas", page_icon="💎",layout="wide")

st.title("Calculadora de Metas")

grid_1,grid_2,spacer = st.columns([1,1,5],gap="small",vertical_alignment="center")

lista_de_variaveis = ["meta_rede"]
iniciar_variaveis(lista_de_variaveis)
   
meta_rede_display = imprimir_metric("meta_rede","Meta Rede",grid_1)
rede_popover = imprimir_popover("Meta Rede (R$)","meta_rede", grid_2)