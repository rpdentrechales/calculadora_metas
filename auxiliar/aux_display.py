import streamlit as st

def atualizar_valores(update_var,update_arg,update_value):
    st.session_state[update_var][update_arg] = st.session_state[update_value]