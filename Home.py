import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="👋",
    layout="wide",
)

col1, col2 = st.columns(2)

with col1:
    st.image('Safe-cuate.png')

with col2:
    st.title("AI Risk Learning Platform")
    st.write('''This is an AI risk learning platform to help you understand vulnerabilities/concerns in AI models and what techniques 
             you can implement in your code to mitigate them. Through this course, wou will learn how to implement privacy-preserving techniques
             including: differential privacy, synthetic data, and homomorphic encryption.''')
    
course1, course2, course3, course4 = st.columns(4)

with course1:
    st.image('Picture1.png')
with course2:
    st.image('Picture2.png')
with course3:
    st.image('Picture3.png')
with course4:
    st.image('Picture4.png')