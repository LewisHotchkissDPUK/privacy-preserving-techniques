import streamlit as st
from streamlit_extras.jupyterlite import jupyterlite

st.set_page_config(
    page_title="Practice Environment",
    page_icon="👋",
)

st.title("Practice Environment")

jupyterlite(1500, 1600)