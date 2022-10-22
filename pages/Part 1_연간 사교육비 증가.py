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

## part 1
# 학교급 사교육 참여율 비교 
df_participation_ratio = pd.read_csv('data/region_subject_ratio.csv',encoding='cp949',index_col=0)

st.header("1️⃣ Part 1 : 지역별 사교육 참여율 변화")
st.markdown("## 🔢 Dataset ")
st.dataframe(df_participation_ratio)
st.markdown("---")
st.markdown("### 📶 각 지역의 과목별 사교육 참여율 및 월 평균 지출비용 비교")
HtmlFile_regratio = open("data/df_region_subject_chart.html", 'r', encoding='utf-8')
source_code_regratio = HtmlFile_regratio.read() 
print(source_code_regratio)
components.html(source_code_regratio,height=600)

## part 2 
# 연간 1인당 월 평균 사교육비 지출의 변화를 지역-학교급-과목별로 분석 
 
# 사교육비 데이터 로드
@st.cache(allow_output_mutation=True)
def load_private_data():
    data = pd.read_csv("https://raw.githubusercontent.com/wumusill/Structure/main/dataset/seoul_private.csv")
    data = data.drop([0, 1, 2])
    return data

st.markdown("### 📶 서울시의 1인당 월평균 지출 사교육비 비교 (단위 :만원)")
private_data = load_private_data()
private_data.columns = ["시점", "평균 사교육비", "평균 사교육 참여율(%)", 
                    "초등학교 사교육비", "초등 사교육 참여율(%)", 
                    "중학교 사교육비", "중등 사교육 참여율(%)", 
                    "고등학교 사교육비", "고등 사교육 참여율(%)", 
                    "일반고 사교육비", "일반고 사교육 참여율(%)"]
private_data = private_data.astype('float')

condition = private_data.columns.str.contains("사교육비")
ratio_df = private_data.loc[:, ~condition]
ratio_df.index = ["11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"]

cost_df = private_data.loc[:, condition]
cost_df.index = ["11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"]



# 1인당 평균 사교육비 그래프
if st.checkbox('Show Code'):
    with st.echo():
        plt.set_loglevel('WARNING')
        fig1 = plt.figure(figsize=(10, 5))
        sns.lineplot(data=cost_df, x=cost_df.index, y="평균 사교육비", label="평균")
        sns.lineplot(data=cost_df, x=cost_df.index, y="초등학교 사교육비", label="초등학교")
        sns.lineplot(data=cost_df, x=cost_df.index, y="중학교 사교육비", label="중학교")
        sns.lineplot(data=cost_df, x=cost_df.index, y="고등학교 사교육비", label="고등학교")
        sns.lineplot(data=cost_df, x=cost_df.index, y="일반고 사교육비", label="일반고")
        plt.legend(bbox_to_anchor=(1, 1))
        plt.title("1인당 평균 사교육비 (만원)")
        plt.axvline(x = '15',linestyle='--')
        plt.axvline(x = '19',linestyle='--')

        # 사교육 참여율 그래프
        fig2 = plt.figure(figsize=(10, 5))
        sns.lineplot(data=ratio_df, x=ratio_df.index, y="평균 사교육 참여율(%)", label="평균")
        sns.lineplot(data=ratio_df, x=ratio_df.index, y="초등 사교육 참여율(%)", label="초등")
        sns.lineplot(data=ratio_df, x=ratio_df.index, y="중등 사교육 참여율(%)", label="중등")
        sns.lineplot(data=ratio_df, x=ratio_df.index, y="고등 사교육 참여율(%)", label="고등")
        sns.lineplot(data=ratio_df, x=ratio_df.index, y="일반고 사교육 참여율(%)", label="일반고")
        plt.legend(bbox_to_anchor=(1, 1))
        plt.title("사교육 참여율 (%)")
        plt.axvline(x = '15',linestyle='--')
        plt.axvline(x = '19',linestyle='--')# Layout

plt.set_loglevel('WARNING')
fig1 = plt.figure(figsize=(10, 5))
sns.lineplot(data=cost_df, x=cost_df.index, y="평균 사교육비", label="평균")
sns.lineplot(data=cost_df, x=cost_df.index, y="초등학교 사교육비", label="초등학교")
sns.lineplot(data=cost_df, x=cost_df.index, y="중학교 사교육비", label="중학교")
sns.lineplot(data=cost_df, x=cost_df.index, y="고등학교 사교육비", label="고등학교")
sns.lineplot(data=cost_df, x=cost_df.index, y="일반고 사교육비", label="일반고")
plt.legend(bbox_to_anchor=(1, 1))
plt.title("1인당 평균 사교육비 (만원)")
plt.axvline(x = '15',linestyle='--')
plt.axvline(x = '19',linestyle='--')

# 사교육 참여율 그래프
fig2 = plt.figure(figsize=(10, 5))
sns.lineplot(data=ratio_df, x=ratio_df.index, y="평균 사교육 참여율(%)", label="평균")
sns.lineplot(data=ratio_df, x=ratio_df.index, y="초등 사교육 참여율(%)", label="초등")
sns.lineplot(data=ratio_df, x=ratio_df.index, y="중등 사교육 참여율(%)", label="중등")
sns.lineplot(data=ratio_df, x=ratio_df.index, y="고등 사교육 참여율(%)", label="고등")
sns.lineplot(data=ratio_df, x=ratio_df.index, y="일반고 사교육 참여율(%)", label="일반고")
plt.legend(bbox_to_anchor=(1, 1))
plt.title("사교육 참여율 (%)")
plt.axvline(x = '15',linestyle='--')
plt.axvline(x = '19',linestyle='--')# Layout
        
container1 = st.container()
col1, col2 = st.columns(2)

with container1:
    with col1:
        fig1
    with col2:
        fig2
