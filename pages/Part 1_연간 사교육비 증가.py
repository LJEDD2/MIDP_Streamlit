import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit as st
import time
import koreanize_matplotlib
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout='wide')

## part 1
# 학교급 사교육 참여율 비교 
df_participation_ratio = pd.read_csv('data/region_subject_ratio.csv',encoding='cp949',index_col=0)

st.header("Part 1 : 지역별 사교육 참여율 변화")
st.dataframe(df_participation_ratio)
st.markdown("---")
st.markdown("### 📶 각 지역의 과목별 사교육 참여율 및 월 평균 지출비용 비교")
HtmlFile_regratio = open("data/df_region_subject_chart.html", 'r', encoding='utf-8')
source_code_regratio = HtmlFile_regratio.read() 
print(source_code_regratio)
components.html(source_code_regratio,height=500)

## part 2 
# 연간 1인당 월 평균 사교육비 지출의 변화를 지역-학교급-과목별로 분석 
 
