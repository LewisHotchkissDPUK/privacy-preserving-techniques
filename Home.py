import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="👋",
    layout="wide",
)

st.title("AI Risk Learning Platform")

col1, col2 = st.columns(2)

with col1:
    st.image('Safe-cuate.png')

with col2:
    st.write("This is an AI risk learning platform to help you understand vulnerabilities in AI models and what techniques you can implement in your code to mitigate them")