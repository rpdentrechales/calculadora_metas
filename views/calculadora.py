import streamlit as st
import pandas as pd
import datetime
from auxiliar.aux_display import *

st.set_page_config(page_title="Calculadora de Metas", page_icon="💎",layout="wide")

column_top = st.columns([4,1])

column_top[0].title("Calculadora de Metas")
column_top[1].button("Calcular Valores")

st.header("Metas Totais")

grid = st.columns(6,gap="small",vertical_alignment="center")

lista_de_variaveis = ["total_rede","total_fb","total_google"]
iniciar_variaveis(lista_de_variaveis)
   
imprimir_metric("total_rede","Total Rede",grid[0])
imprimir_popover("Total Rede (R$)","total_rede", grid[1])

imprimir_metric("total_google","Total Google",grid[2])
imprimir_popover("Total Google (R$)","total_google", grid[3])

imprimir_metric("total_fb","Total Facebook",grid[4])
imprimir_popover("Total Facebook (R$)","total_fb", grid[5])