import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import koreanize_matplotlib
import streamlit.components.v1 as components
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


st.markdown("2️⃣ Part 2. 연간 사교육비 지출 유형 비교 ")