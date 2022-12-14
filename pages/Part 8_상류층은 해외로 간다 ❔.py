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

st.header("8οΈβ£ μμΈμ κ° μ§μ­ μ€ ν΄μΈ μ ν λΉμ¨μ΄ κ°μ₯ λμ λλ€λβ")

# @st.cache(allow_output_mutation=True)
def load_go_abroad_ratio():
    ratio = pd.read_csv("https://raw.githubusercontent.com/wumusill/Structure/main/dataset_eda/go_abroad_ratio.csv")
    return ratio


ratio = load_go_abroad_ratio()
ratio = ratio.set_index("μμ ")
ratio = ratio.astype("float")

drop_condition = ~ratio.columns.str.contains("μκ³")
ratio = ratio.loc[:, drop_condition]


st.markdown("### π½ νκ΅κΈλ³ μμΈμ μμΉκ΅¬λ³ ν΄μΈ μ νμμ λΉμ¨ λ³ν")
# νκ΅ μ‘°κ±΄
selected_school = st.selectbox("νκ΅", ["μ΄λ±νκ΅", "μ€νκ΅", "κ³ λ±νκ΅"])
condition = ratio.columns.str.contains(f"{selected_school}")
school_data = ratio.loc[:, condition]

if st.checkbox('Show data', key = 123):
    st.subheader('data')
    st.write(school_data)


st.markdown("#### μ‘°νν  μ°λ")
# μ°λ μ‘°κ±΄
year_to_filter = st.slider('μ°λ', 2012, 2020, 2015)
year_condition = school_data.index == year_to_filter
year_school_data = school_data[year_condition].T

df_temp = year_school_data
df_temp = df_temp.reset_index()
df_temp = df_temp.rename(columns={'index':'name'})
df_temp = df_temp.drop(0)
df_temp["name"] = df_temp["name"].map(lambda x: x.split()[0])
df_temp


st.markdown("##### μκ°ν")
m = folium.Map(location=[37.566345, 127.4],
    zoom_start = 11,
    tiles = 'Stamen Terrain')

# κ΅¬λ³ μκ²½λ json
geo_url = 'https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json'
response = requests.get(geo_url)
geo_json = json.loads(response.content)


folium.GeoJson(geo_json,
              name="μ§μ­κ΅¬").add_to(m)


# νμ κ΅¬μ­ κ²½κ³ νμ, μ€λ¨μ¨ μμΉ 
m.choropleth(geo_data=geo_json,
                 name="μ§μ­κ΅¬",
                 data=df_temp,
                 columns=[df_temp.columns[0], df_temp.columns[1]],
                 key_on="properties.name",
                 fill_color='YlGn',
                 fill_opacity=0.7,
                 line_opacity=0.2,
                 legend_name=""
                 )


# μΆλ ₯
st_data = st_folium(m, width=2100)

st.markdown("### π μ¬λ―Έμλ μΈμ¬μ΄νΈ : νμ μ€λ¨μ¨μ΄ λμ μ΄μ λ ν΄μΈ μ ν λλ¬Έ β")
st.markdown(" π κ°λ¨κ΅¬ μΌλμ ν΄μΈ μ νμ μμ νμ μ€λ¨μ¨μ΄ λμμ‘μΌλ©°, λ κ°μ€ κ°μ λμ μμ μκ΄κ΄κ³κ° λνλ¬λ€.\n\n"
            "λμ΄ λ§μ κ°λ¨ μλ―Όλ€μ΄ μλλ€μ ν΄μΈμμ κ΅μ‘μ μν€κ³  μλ€λΌκ³  μΆμΈ‘μ ν΄λ³Ό μ μκ² μ§λ§, μ΄ μλ£κ° νμ μ±μ·¨λκ° λ?μμ§ κ²κ³Ό μΈκ³Όμ±μ΄ μλ€κ³  λ¨μΈν  μλ μλ€.")
# img_27 = Image.open("Result/μ¬λΌμ΄λ27.png")
# st.image(img_27,width=1000)
# img_28 = Image.open("Result/μ¬λΌμ΄λ28.png")
# st.image(img_28,width=1500)

def load_go_abroad_corr():
    data = pd.read_csv("https://raw.githubusercontent.com/wumusill/Structure/main/dataset_eda/go_abroad_corr.csv")
    return data


# λ°μ΄ν° λ‘λ
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