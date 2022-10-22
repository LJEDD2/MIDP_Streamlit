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

st.header("4️⃣ Part 4 : 청소년 학업 인식 수준 변화")
st.markdown("중-고등학생의 진학 진로 선택 기준의 변화와 희망하는 직업의 유무, 희망하는 최종 학력 수준에 대해 분석")
st.markdown("---")
st.markdown("### 📶중-고등학생의 진학 학교 및 진로 선택 기준")

HtmlFile_2 = open("data/df_korea_student.html", 'r', encoding='utf-8')
source_code_2 = HtmlFile_2.read() 
print(source_code_2)
components.html(source_code_2,height=500)
st.markdown("---")
st.markdown("### 📶학교급별 희망하는 직업 유무와 희망하는 최종 학력 수준")
HtmlFile_1 = open("data/df_survey_by_school_level.html", 'r', encoding='utf-8')
source_code_1 = HtmlFile_1.read() 
print(source_code_1)
components.html(source_code_1,height=800)

