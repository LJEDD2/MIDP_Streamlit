import folium
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import json
import time
from streamlit_folium import st_folium
import koreanize_matplotlib

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

st.header("5οΈβ£ Part 5. μμΈμ κ° μ§μ­λ³ νμ μ€λ¨μ¨μ λ³ν")

# DATA_URL = "data/seoul_stop_school.csv"

# @st.cache(allow_output_mutation=True)
# def load_data():
#     data = pd.read_csv(DATA_URL)
#     data.index = ["2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"]
#     data = data.astype("float")
#     return data


data = pd.read_csv("data/seoul_stop_school.csv")
data.index = ["2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"]
data = data.astype("float")

st.markdown("### π½ νκ΅κΈ μ ν ")
# νκ΅ μ‘°κ±΄
selected_school = st.selectbox("νκ΅", ["μ΄λ±νκ΅", "μ€νκ΅", "κ³ λ±νκ΅"])
condition = data.columns.str.contains(f"{selected_school} νμμ€λ¨μ¨")
school_data = data.loc[:, condition]

if st.checkbox('Show data'):
    st.subheader('data')
    st.write(school_data)


st.markdown("#### μ‘°νν  μ°λ")
# μ°λ μ‘°κ±΄
year_to_filter = st.slider('μ°λ', 2011, 2020, 2015)
year_condition = school_data.index == str(year_to_filter)
year_school_data = school_data[year_condition].T

df_temp = year_school_data
df_temp = df_temp.reset_index()
df_temp = df_temp.rename(columns={'index':'name'})
df_temp = df_temp.drop(0)
df_temp["name"] = df_temp["name"].map(lambda x: x.split()[0])
# df_temp


st.markdown("## μκ°ν")
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
                 legend_name="κ΅¬λ³ νμ μ€λ¨μ¨"
                 )
# μΆλ ₯
st_data = st_folium(m, width=2100)
