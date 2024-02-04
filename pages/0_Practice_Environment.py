import streamlit as st
#from streamlit_extras.jupyterlite import jupyterlite
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Practice Environment",
    page_icon="👋",
)

st.title("Practice Environment")

components.iframe(
    "https://jupyterlite.github.io/demo/repl/index.html?kernel=python&toolbar=1",
    height=500
)