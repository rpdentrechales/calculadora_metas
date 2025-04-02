import streamlit as st

# --- PAGE SETUP ---
calculadora_page = st.Page(
    "views/calculadora.py",
    title="Calculadora de metas",
    icon=":material/calculate:",
    default=True,
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Pages": [calculadora_page]
    }
)


# --- SHARED ON ALL PAGES ---
# st.logo("assets/codingisfun_logo.png")


# --- RUN NAVIGATION ---
pg.run()
