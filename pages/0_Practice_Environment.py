import streamlit as st
#from streamlit_extras.jupyterlite import jupyterlite
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Practice Environment",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state='collapsed'
)

st.title("Practice Environment")

col1, col2 = st.columns(2)

with col1:
    with st.container(height=600):
        st.header('Creating Synthetic Data')

        st.write("In this tutorial, we'll use the SDV to create synthetic data for a single table and evaluate it. The SDV uses machine learning to learn patterns from real data and emulates them when creating synthetic data. We'll use the **CTGAN** algorithm to do this. CTGAN uses generative adversarial networks (GANs) to create synthesise data with high fidelity.")


        st.subheader('Load demo data')

        code = '''from sdv.datasets.demo import download_demo

real_data, metadata = download_demo(
    modality='single_table',
    dataset_name='fake_hotel_guests'
)
        '''

        st.code(code)

        st.write("Now visualise this metadata")

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

    

    

if st.button("Next"):
    st.write()


#from streamlit_ace import st_ace
#content = st_ace()