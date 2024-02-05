import streamlit as st
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm, rcParams
import pandas as pd
import time
import streamlit_extras

from st_clickable_images import clickable_images


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

#from streamlit_player import st_player
#st_player("https://youtu.be/y5IQZRCyBts")

from streamlit_ace import st_ace
content = st_ace()
content

#video_file = open('Pictures/SyntheticData.mp4', 'rb')
#video_bytes = video_file.read()

#st.video(video_bytes)