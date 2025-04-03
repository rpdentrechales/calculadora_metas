import streamlit as st

def atualizar_valores(update_var,update_arg,update_value):
    st.session_state[update_var][update_arg] = st.session_state[update_value]

def imprimir_metric(nome_metrica,label_metrica,grid):
    dados_da_metrica = st.session_state[nome_metrica]
    dont_use = dados_da_metrica["dont_use"]

    if dont_use:
        valor = "calcular"
    else:
        valor = dados_da_metrica["value"]

    return grid.metric(label=label_metrica,value=valor)
