import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="👋",
    layout="wide",
)

from PIL import Image
with st.sidebar.container():
    image = Image.open("Pictures/Picture8.png")
    st.image(image, use_column_width=True)

col1, col2 = st.columns(2)

with col1:
    st.image('Safe-cuate.png')

with col2:
    st.title("AI Risk Learning Platform")
    st.write('''This is an AI risk learning platform to help you understand vulnerabilities/concerns in AI models and what techniques 
             you can implement in your code to mitigate them. Through this course, wou will learn how to implement privacy-preserving techniques
             including: differential privacy, synthetic data, and homomorphic encryption. Throughout the course, you will be able to try practical activities to implement some of these techniques yourself
             and run built-in attacks to evaluate their effectiveness.''')
    
    st.button("Start Now")
    
st.write("")
st.write("")
st.write("")
st.write("")

course1, course2, course3, course4 = st.columns(4)

with course1:
    st.image('Pictures/Picture1.png')
with course2:
    st.image('Pictures/Picture2.png')
with course3:
    st.image('Pictures/Picture3.png')
with course4:
    st.image('Pictures/Picture4.png')