import streamlit as st
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm, rcParams
import pandas as pd
import time

st.set_page_config(
    page_title="Evaluation",
    page_icon="👋",
    layout="wide",
)

from PIL import Image
with st.sidebar.container():
    image = Image.open("Pictures/Picture8.png")
    st.image(image, use_column_width=True)

st.title("Synthetic Data Evaluation")

uploaded_file = st.file_uploader("Upload a CSV Dataset", type=["csv"])

if uploaded_file:

    data = pd.read_csv(uploaded_file)
    
    col1, col2 = st.columns(2)
    
    with col1:
        discrete_cols = st.multiselect("Select discrete columns", data.columns)
        identifier_col = st.selectbox("Select identifier column", data.columns)
    
    with col2:
        prediction_col = st.selectbox("Select prediction column for evaluation", data.columns)
        noise_level = st.slider("Select noise level", 0, 10, 1)
    
    if st.button("Submit"):

        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)

        eval_coll, eval_col2 = st.columns(2)

        with eval_coll:
            points =[(76, 66)]

            x = list(map(lambda x: x[0], points))
            y = list(map(lambda x: x[1], points))

            font_path = "Poppins-SemiBold.ttf"
            prop = fm.FontProperties(fname=font_path)
            rcParams["font.family"] = prop.get_name()

            plt.rc('grid', linestyle="-", color='white', linewidth=1, alpha=1)
            plt.figure(figsize=(6, 6), facecolor="#050526")
            plt.gca().set_facecolor('#050526')
            plt.xlim(0, 100)
            plt.ylim(0, 100)
            plt.xticks(range(0, 101, 20), color='white')
            plt.yticks(range(0, 101, 20), color='white')
            plt.scatter(x, y, color= '#ffe342', s=250, alpha=1, zorder=3)  #4246ff 2024c9
            plt.xlabel('LOW PRIVACY', color='white', fontproperties=prop)
            plt.ylabel('LOW UTILITY', color='white', fontproperties=prop)
            plt.text(0.5, 1.05, 'HIGH PRIVACY', color='white', ha='center', va='center', fontproperties=prop, transform=plt.gca().transAxes)
            plt.text(1.05, 0.5, 'HIGH UTILITY', color='white', ha="center", va='center', rotation=-90, fontproperties=prop, transform=plt.gca().transAxes)

            ax = plt.gca()
            for axis in['top', 'bottom', 'left', 'right']:
                ax.spines[axis].set_color('white')
                ax.spines[axis].set_linewidth(2)

            plt.plot([0,100],[100,0],color='#121470', linestyle='--')
            
            plt.grid(True)
            plt.savefig("figure.png")
            st.image("figure.png")

        with eval_col2:
            st.write("")
            st.title("Evaluation Metrics")
            st.metric("Membership Inference Attack", 0.68)
            st.metric("Classification F1-Score", 0.75)
            st.metric("Similarity Score", 0.82)
