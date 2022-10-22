import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import time

df_agg = pd.read_csv("data/grade_num.csv", encoding="cp949")
df_agg["연도"] = df_agg["연도"].astype(int)

st.set_page_config(
    page_title="9조 streamlit_page",
    page_icon="🖍",
    layout="wide",
)
# 페이지 로드 진행 상황 바
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

st.header("7️⃣ Part 7 : 학업 성취도 우수 학생의 수 변화")
st.markdown("❓학업 성적이 우수한 학생들의 수가 실제로 감소했을까 ?")
st.markdown("---")


st.markdown("### 💯연간 각 과목별 청소년 학업 성취도 변화")
st.markdown("#### 📶 학업성취도 우수학생 수")

st.sidebar.header('🔽 학교급 선택 :')

selected_school = st.sidebar.selectbox('중학교 | 고등학교',
   ["중학교", "고등학교"])


if selected_school == "중학교":
    fig1_1 = px.line(df_agg, x="연도", y="3수준학생수(중)"
                , color="과목", markers=True)
    fig1_1.update_layout(autosize=False,
    width=1000,
    height=800)
    fig1_1.add_vline(x=2020, line_width=3, line_dash="dash", line_color="black")
    st.plotly_chart(fig1_1)

elif selected_school == "고등학교":
    fig1_2 = px.line(df_agg, x="연도", y="3수준학생수(고)"
                , color="과목", markers=True)
    fig1_2.update_layout(autosize=False,
    width=1000,
    height=800)
    fig1_2.add_vline(x=2020, line_width=3, line_dash="dash", line_color="black")
    st.plotly_chart(fig1_2)

st.markdown("#### 📶 학업성취도 열등학생 수")

if selected_school == "중학교":
    fig2_1 = px.line(df_agg, x="연도", y="1수준학생수(중)"
                , color="과목", markers=True)
    fig2_1.update_layout(autosize=False,
    width=1000,
    height=800)
    fig2_1.add_vline(x=2020, line_width=3, line_dash="dash", line_color="black")
    st.plotly_chart(fig2_1)

elif selected_school == "고등학교":
    fig2_2 = px.line(df_agg, x="연도", y="1수준학생수(고)"
                , color="과목", markers=True)
    fig2_2.update_layout(autosize=False,
    width=1000,
    height=800)
    fig2_2.add_vline(x=2020, line_width=3, line_dash="dash", line_color="black")
    st.plotly_chart(fig2_2)