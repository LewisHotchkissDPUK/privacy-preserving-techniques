import streamlit as st
#from streamlit_extras.jupyterlite import jupyterlite
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Practice Environment",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state='collapsed'
)

from PIL import Image
with st.sidebar.container():
    image = Image.open("Pictures/Picture8.png")
    st.image(image, use_column_width=True)

st.title("Practice Environment")

col1, col2 = st.columns(2)

with col1:
    with st.container(height=600):
        st.header('Creating Synthetic Data')

        st.write("In this tutorial, we'll use the SDV package to create synthetic data for a table and evaluate it. SDV uses machine learning to learn patterns from real data and emulates them when creating synthetic data. In this example, we will use **CTGAN** to create synthetic data with high fidelity.")


        st.subheader('Load demo data')

        code = '''data = pd.read_csv("dementia_dataset.csv")
        '''

        st.code(code)

        st.write("Now detect the metadata from the data")

        code2 = '''from sdv.metadata import SingleTableMetadata
metadata = SingleTableMetadata()
metadata.detect_from_dataframe(data)
metadata'''

        st.code(code2)

        st.write("Visualise this metadata")

        with st.expander("Reveal Answer"):
            st.write()
            st.code('''metadata.visualize()''')

        st.subheader("Train a synthesiser")
        st.write("An SDV **synthesizer** is an object that you can use to create synthetic data. It learns patterns from the real data and replicates them to generate synthetic data.")

        synth_code = '''from sdv.single_table import CTGANSynthesizer

synthesizer = CTGANSynthesizer(metadata)
synthesizer.fit(real_data)'''

        st.code(synth_code)

with col2:
    #components.iframe(
    #    "https://jupyterlite.github.io/demo/repl/index.html?kernel=python&toolbar=1",
    #    height=600
    #)

    #components.iframe(
    #    "https://jupyter.org/try-jupyter/lab/index.html",
    #    height=600
    #)

    components.iframe(
        "https://jupyterlite.readthedocs.io/en/stable/_static/notebooks/?path=intro.ipynb",
        height=600
    )

    

button_col1, button_col2 = st.columns([1,1])   

with button_col1:
    if st.button("Back", use_container_width=True):
        switch_page("Home")

with button_col2:
    if st.button("Next", use_container_width=True):
        switch_page("Resources")


#from streamlit_ace import st_ace
#content = st_ace()