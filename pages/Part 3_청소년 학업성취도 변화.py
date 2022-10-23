import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import koreanize_matplotlib
import streamlit.components.v1 as components
import time


# 페이지 로드 진행 상황 바
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

st.header("3️⃣ Part 3 : 청소년 국내외 학업 성취도 수준의 하락세")
st.markdown("국내 학업성취도의 경우 2016년 까지 전국 모든 학교에서 실시하여 지역별 데이터가 있지만,"
            "\n\n 2017년 이후 학교 줄 세우기 논란에 의해 전국 3% 표집 평가로 지역별 데이터를 구하기가 힘들어졌다."
            "\n\n 따라서, 서울 데이터가 전국 데이터와 큰 차이를 보이지 않아 전국 데이터로 분석을 진행하였다. ")
st.markdown("---")

st.markdown("## 💹 PISA Score")
st.markdown("### 연간 국제 학업 성취도 수준의 변화 ")
st.markdown("#### : Reading - Math - Science ")

# 국제 학업성취도 성적
# 국어 로드
# @st.cache(allow_output_mutation=True)
# def load_national_reading():
#     data = pd.read_excel("data/international_test.xls", sheet_name=0, engine='openpyxl')
#     return data

national_reading = pd.read_excel("data/international_test.xlsx", sheet_name=0)
national_reading[["Average", "Standard Error"]] = national_reading[["Average", "Standard Error"]].astype("float")


# 수학 로드
# @st.cache(allow_output_mutation=True)
# def load_national_math():
#     data = pd.read_excel("data/international_test.xls", sheet_name=1, engine='openpyxl')
#     return data

national_math = pd.read_excel("data/international_test.xlsx", sheet_name=1)
national_math[["Average", "Standard Error"]] = national_math[["Average", "Standard Error"]].astype("float")


# # 과학 로드
# @st.cache(allow_output_mutation=True)
# def load_national_science():
#     data = pd.read_excel("data/international_test.xls", sheet_name=2, engine='openpyxl')
#     return data

national_science = pd.read_excel("data/international_test.xlsx", sheet_name=2)
national_science[["Average", "Standard Error"]] = national_science[["Average", "Standard Error"]].astype("float")

# 읽기 top5
reading_top5 = national_reading.sort_values(["Year/Study", "Average"], ascending=[True, False])
reading_top5 = reading_top5.groupby("Year/Study").head()

# 수학 top5
math_top5 = national_math.sort_values(["Year/Study", "Average"], ascending=[True, False])
math_top5 = math_top5.groupby("Year/Study").head()

# 과학 top5
science_top5 = national_science.sort_values(["Year/Study", "Average"], ascending=[True, False])
science_top5 = science_top5.groupby("Year/Study").head()


st.markdown("↔️그래프에 마우스를 올리면 확대 가능")
# 읽기 시각화
reading = sns.lmplot(data=reading_top5, x="Year/Study", y="Average", hue='Jurisdiction', ci=None)
fig_reading = reading.fig
plt.title("reading score")

# 수학 시각화
math = sns.lmplot(data=math_top5, x="Year/Study", y="Average", hue='Jurisdiction', ci=None)
fig_math = math.fig
plt.title("math score")

# 과학 시각화
science = sns.lmplot(data=science_top5, x="Year/Study", y="Average", hue='Jurisdiction', ci=None)
fig_science = science.fig
plt.title("science score")


# Layout
container2 = st.container()
col3, col4, col5 = st.columns(3)

with container2:
    with col3:
        fig_reading
    with col4:
        fig_math
    with col5:
        fig_science


st.markdown("---")
st.markdown("### 📶중-고등학생 국내 학업성취도 변화")
st.markdown("↔️그래프에 마우스를 올리면 확대 가능")
# # 중등 로드
# @st.cache(allow_output_mutation=True)
# def load_kr_mid_test():
#     data = pd.read_excel("data/kr_test.xls", sheet_name="중등", engine='openpyxl')
#     return data


# # 고등 로드
# @st.cache(allow_output_mutation=True)
# def load_kr_high_test():
#     data = pd.read_excel("data//kr_test.xls", sheet_name="고등", engine='openpyxl')
#     return data

# 데이터 로드
kr_mid_test = pd.read_excel("data/kr_test.xlsx", sheet_name="중등")
kr_high_test = pd.read_excel("data//kr_test.xlsx", sheet_name="고등")

# 사이드바 검색 기능
st.sidebar.header("성취 수준별 데이터 시각화")
st.sidebar.text("3수준 🔜 1수준 : 상위권 🔜 하위권")
# 수준 검색
l = ["3수준", "2수준", "1수준"]
# l.append("All")
selected_level = st.sidebar.selectbox("Level", l)


mid_3 = sns.lmplot(data=kr_mid_test, x="연도", y=selected_level, hue='과목', ci=None)
fig_mid_3 = mid_3.fig
plt.title(f"국내 중학생 학업성취도 평가 {selected_level}")


high_3 = sns.lmplot(data=kr_high_test, x="연도", y=selected_level, hue='과목', ci=None)
fig_high_3 = high_3.fig
plt.title(f"국내 고등학교 학업성취도 평가 {selected_level}")

# Layout
container3 = st.container()
col6, col7 = st.columns(2)

with container3:
    with col6:
        fig_mid_3
    with col7:
        fig_high_3

st.markdown("---")       