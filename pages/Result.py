import folium
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import json
from streamlit_folium import st_folium
import koreanize_matplotlib
from PIL import Image
import time

st.set_page_config(
    page_title="9μ‘° streamlit_page",
    page_icon="π",
    layout="wide",
) # μΉνμ΄μ§ ν­ λμμΈ μ€μ 

# νμ΄μ§ λ‘λ μ§ν μν© λ°
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

st.header("π‘RESULT")


img_30 = Image.open("Result/μ¬λΌμ΄λ30.png")
st.image(img_30,width=1200)
img_31 = Image.open("Result/μ¬λΌμ΄λ31.png")
st.image(img_31,width=1200)
img_32 = Image.open("Result/μ¬λΌμ΄λ32.png")
st.image(img_32,width=1200)
img_33 = Image.open("Result/μ¬λΌμ΄λ33.png")
st.image(img_33,width=1200)
