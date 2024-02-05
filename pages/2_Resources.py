import streamlit as st
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm, rcParams
import pandas as pd
import time
import streamlit_extras

st.set_page_config(
    page_title="Resources",
    page_icon="👋",
    layout="wide",
)

from PIL import Image
with st.sidebar.container():
    image = Image.open("Pictures/Picture8.png")
    st.image(image, use_column_width=True)

st.title("Synthetic Data Resources")

#video_file = open('Pictures/SyntheticData.mp4', 'rb')
#video_bytes = video_file.read()

#st.video(video_bytes)