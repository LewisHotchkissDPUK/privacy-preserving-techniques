import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="👋",
)

st.title("AI Risk Learning Platform")

col1, col2 = st.columns(2)

with col1:
    st.image('Safe-cuate.png')