import streamlit as st
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm, rcParams

st.title("Synthetic Data Generation")

uploaded_file = st.file_uploader("Upload a CSV Dataset", type=["csv"])

if uploaded_file:
    
    col1, col2 = st.columns(2)
    
    with col1:
        discrete_cols = st.multiselect("Select discrete columns", ['col1','col2'])
    
    with col2:
        noise_level = st.slider("Select noise level", 0, 10, 1)
    
    if st.button("Submit"):
        eval_coll, eval_col2 = st.columns(2)

        with eval_coll:
            points =[(34, 64)]

            x = list(map(lambda x: x[0], points))
            y = list(map(lambda x: x[1], points))

            font_path = "Poppins-SemiBold.ttf"
            prop = fm.FontProperties(fname=font_path)
            rcParams["font.family"] = prop.get_name()

            plt.rc('grid' linestyle="-", color='white', linewidth=1, alpha=1)
            plt.figure(figsize=(6, 6), facecolor="#330930")
            plt.gca().set_facecolor('#33093D')
            plt.xlim(0, 100)
            plt.ylim(0, 100)
            plt.xticks(range(0, 101, 20), color='white')
            plt.yticks(range(0, 101, 20), color='white')
            plt.scatter(x, y, color= '#cc1d6e' s=200, alpha=1, zorder=3)
            plt.xlabel('LOW PRIVACY', color='white', fontproperties=prop)
            plt.ylabel('LOW UTILITY', color='white', fontproperties=prop)
            plt.text(0.5, 1.05, 'HIGH PRIVACY', color='white', ha='center', va='center', fontproperties=prop, transform=plt.gca().transAxes)
            plt.text(1.05, 0.5, 'HIGH UTILITY', color='white', ha="center", va='center', rotation=-90, fontproperties=prop, transform=plt.gca().transAxes)

            ax = plt.gca()
            for axis in['top', 'bottom', 'left', 'right']:
                ax.spines[axis].set_color('white')
                ax.spines[axis].set_linewidth(2)

            plt.plot([0,100],[100,0],color='#651D6D', linestyle='--')
            
            plt.grid(True)
            plt.savefig("figure.png")
            st.image("figure.png")
