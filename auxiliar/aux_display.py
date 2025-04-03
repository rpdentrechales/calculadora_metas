import streamlit as st

def atualizar_valores(update_var,update_arg,update_value):
    st.session_state[update_var][update_arg] = st.session_state[update_value]

def imprimir_metric(nome_metrica,label_metrica,grid):
    dados_da_metrica = st.session_state[nome_metrica]
    dont_use = dados_da_metrica["dont_use"]

    if dont_use:
        display = "calcular"
    else:
        valor = dados_da_metrica["value"]
        display = f"R$ {valor:.2f}"

    return grid.metric(label=label_metrica,value=display)


def imprimir_popover(label,key, grid):
    popover= grid.popover("Ajustar")

    number_input_key = f"{key}_number"
    toggle_input_key = f"{key}_toggle"

    popover.number_input(label=label,
                                        min_value=0.0,
                                        value=None,
                                        on_change=atualizar_valores,
                                        key=number_input_key,
                                        kwargs = {"update_var":key,
                                                    "update_arg":"value",
                                                    "update_value":number_input_key})

    popover.toggle(label="Calcular depois",
                                        value=True,
                                        on_change=atualizar_valores,
                                        key=toggle_input_key,
                                        kwargs = {"update_var":key,
                                                    "update_arg":"dont_use",
                                                    "update_value":toggle_input_key})
    
    return popover


def iniciar_variaveis(lista_de_variaveis):

    for key in lista_de_variaveis:

        if key in st.session_state:
            
            variavel = st.session_state[key]

        else:
            variavel = {"value":0,
                            "dont_use":True}
            st.session_state[key] = variavel
    
    return