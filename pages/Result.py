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
    page_title="9조 streamlit_page",
    page_icon="🖍",
    layout="wide",
) # 웹페이지 탭 디자인 설정

# 페이지 로드 진행 상황 바
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

st.header("💡RESULT")


img_30 = Image.open("Result/슬라이드30.png")
st.image(img_30,width=1200)
img_31 = Image.open("Result/슬라이드31.png")
st.image(img_31,width=1200)
img_32 = Image.open("Result/슬라이드32.png")
st.image(img_32,width=1200)
img_33 = Image.open("Result/슬라이드33.png")
st.image(img_33,width=1200)
