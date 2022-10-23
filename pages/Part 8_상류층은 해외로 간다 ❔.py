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

st.header("8️⃣ 서울시 각 지역 중 해외 유학 비율이 가장 높은 동네는❓")

# @st.cache(allow_output_mutation=True)
def load_go_abroad_ratio():
    ratio = pd.read_csv("https://raw.githubusercontent.com/wumusill/Structure/main/dataset_eda/go_abroad_ratio.csv")
    return ratio


ratio = load_go_abroad_ratio()
ratio = ratio.set_index("시점")
ratio = ratio.astype("float")

drop_condition = ~ratio.columns.str.contains("소계")
ratio = ratio.loc[:, drop_condition]


st.markdown("### 🔽 학교급별 서울시 자치구별 해외 유학생의 비율 변화")
# 학교 조건
selected_school = st.selectbox("학교", ["초등학교", "중학교", "고등학교"])
condition = ratio.columns.str.contains(f"{selected_school}")
school_data = ratio.loc[:, condition]

if st.checkbox('Show data', key = 123):
    st.subheader('data')
    st.write(school_data)


st.markdown("#### 조회할 연도")
# 연도 조건
year_to_filter = st.slider('연도', 2012, 2020, 2015)
year_condition = school_data.index == year_to_filter
year_school_data = school_data[year_condition].T

df_temp = year_school_data
df_temp = df_temp.reset_index()
df_temp = df_temp.rename(columns={'index':'name'})
df_temp = df_temp.drop(0)
df_temp["name"] = df_temp["name"].map(lambda x: x.split()[0])
df_temp


st.markdown("##### 시각화")
m = folium.Map(location=[37.566345, 127.4],
    zoom_start = 11,
    tiles = 'Stamen Terrain')

# 구별 위경도 json
geo_url = 'https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json'
response = requests.get(geo_url)
geo_json = json.loads(response.content)


folium.GeoJson(geo_json,
              name="지역구").add_to(m)


# 행정구역 경계 표시, 중단율 색칠
m.choropleth(geo_data=geo_json,
                 name="지역구",
                 data=df_temp,
                 columns=[df_temp.columns[0], df_temp.columns[1]],
                 key_on="properties.name",
                 fill_color='YlGn',
                 fill_opacity=0.7,
                 line_opacity=0.2,
                 legend_name=""
                 )


# 출력
st_data = st_folium(m, width=2100)

st.markdown("### 📈 재미있는 인사이트 : 학업 중단율이 높은 이유는 해외 유학 때문 ❓")
st.markdown(" 📝 강남구 일대의 해외 유학생 수와 학업 중단율이 높아졌으며, 두 가설 간의 높은 양의 상관관계가 나타났다.\n\n"
            "돈이 많은 강남 시민들이 자녀들을 해외에서 교육을 시키고 있다라고 추측은 해볼 수 있겠지만, 이 자료가 학업 성취도가 낮아진 것과 인과성이 있다고 단언할 수는 없다.")
# img_27 = Image.open("Result/슬라이드27.png")
# st.image(img_27,width=1000)
# img_28 = Image.open("Result/슬라이드28.png")
# st.image(img_28,width=1500)

def load_go_abroad_corr():
    data = pd.read_csv("https://raw.githubusercontent.com/wumusill/Structure/main/dataset_eda/go_abroad_corr.csv")
    return data


# 데이터 로드
kr_go_abroad_corr = load_go_abroad_corr()
f = kr_go_abroad_corr.corr().iloc[26:, :26]

if st.checkbox('Show data', key = 456):
    st.subheader('data')
    st.write(f)


mask = np.array([[0., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
               [1., 0., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
                [1., 1., 0., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
                [1., 1., 1., 0., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
                [1., 1., 1., 1., 0., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
                [1., 1., 1., 1., 1., 0., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
                [1., 1., 1., 1., 1., 1., 0., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
                [1., 1., 1., 1., 1., 1., 1., 0., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
                [1., 1., 1., 1., 1., 1., 1., 1., 0., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
                [1., 1., 1., 1., 1., 1., 1., 1., 1., 0., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
                [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 0., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
                [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 0., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
                [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 0., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
                [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 0., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
                [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 0., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
                [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 0.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
                [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        0., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
                [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 0., 1., 1., 1., 1., 1., 1., 1., 1.],
                [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 0., 1., 1., 1., 1., 1., 1., 1.],
                [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 0., 1., 1., 1., 1., 1., 1.],
                [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 0., 1., 1., 1., 1., 1.],
                [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 0., 1., 1., 1., 1.],
                [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 0., 1., 1., 1.],
                [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 0., 1., 1.],
                [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 0., 1.],
                [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 0.],])


fig, ax = plt.subplots(figsize=(7, 4))
plt.rc('xtick', labelsize=6) 
plt.rc('ytick', labelsize=6) 

sns.heatmap(f, annot=True, mask=mask, cmap='coolwarm', vmax=1, vmin= -1, annot_kws={"size": 6}, ax=ax)
st.write(fig)