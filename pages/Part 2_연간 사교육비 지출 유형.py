import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import json
import time
import streamlit.components.v1 as components

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


st.title("2οΈβ£ Part 2. μ°κ° μ¬κ΅μ‘λΉ μ§μΆ μ ν λΉκ΅")
st.markdown("---")
st.markdown("### πΆ μ°κ° μ§μ­λ³ μ¬κ΅μ‘ μ°Έμ¬ μ ν λ° μ νκ·  μ§μΆλΉμ© λ³ν")
HtmlFile_p_edu_type = open("data/df_p_edu_type.html", 'r', encoding='utf-8')
source_code_p_edu_type = HtmlFile_p_edu_type.read() 
print(source_code_p_edu_type)
components.html(source_code_p_edu_type,height=700)

st.markdown("---")

def display_time_filters(df):
    year_list = list(df['Year'].unique())[0:-1:3]
    year_list.sort()
    year = st.sidebar.selectbox('Year', year_list, len(year_list)-1)
    st.markdown(f'### πΆ {year}λ μ¬μ€νμ λΆν¬')
    st.markdown( '#### μ κ΅­ μκ΅°κ΅¬λ³ μ¬μ€νμ λΆν¬ μκ°ν')
    return year

def display_map(df, year):
    df = df[(df['Year'] == year)]
    geo_path = "data/skorea-municipalities-2018-geo.json"
    geo_str = json.load(open(geo_path, encoding="utf-8"))

    map = folium.Map(location=[36, 127], zoom_start=7)

    folium.Choropleth(
        geo_data=geo_str,
        data= df,
        columns=['Code', 'Sum'],
        key_on= 'feature.properties.code',
        fill_color='YlGn',
        fill_opacity=0.7,
        line_opacity=0.5,).geojson.add_to(map)
    
    map = st_folium(map, width=700, height=450)

    return year


#Load Data
df = pd.read_csv('data/korea_city.csv',encoding = 'euc-kr',dtype={'Code' : 'str','Year':'str'})
df['Sum'] = df['Sum'].astype(float)

#Display Filters and Map
year = display_time_filters(df)
map_name = display_map(df, year)
