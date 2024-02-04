import streamlit as st
#from streamlit_extras.jupyterlite import jupyterlite
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Practice Environment",
    page_icon="👋",
    layout="wide"
)

st.title("Practice Environment")

col1, col2 = st.columns(2)

with col1:
    st.header('Creating Synthetic Data')

    st.write("First off get started by loading in the original dataset that we will use to feed into the synthesiser")

    code = '''import pandas as pd
pd.read_csv('path/to/dateset.csv')
    '''

    st.code(code)

with col2:
    components.iframe(
        "https://jupyterlite.github.io/demo/repl/index.html?kernel=python&toolbar=1",
        height=600
    )


from streamlit_ace import st_ace
content = st_ace()