import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import cufflinks as cf
import chart_studio
import folium
from folium.plugins import MarkerCluster
import json
import streamlit as st
from streamlit_folium import st_folium
import time
import koreanize_matplotlib
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Bar, Bar3D, Grid, Line, Liquid, Page, Pie, Timeline, Tab, Map, Grid
from pyecharts import options as opts

st.set_page_config(layout='wide')
    
## Title
st.title("내 거친 성적과 불안한 공교육💦")

## Header
st.header("MID PROJECT\n ### : 초중등 시험 폐지 이후 사교육 환경 변화와 원인 분석")
st.text("팀장 : 이정은")
st.text("팀원 : 문영운, 구자현, 안혜윤, 문종현")
st.markdown("---")

st.markdown("## 사용 라이브러리")
with st.echo():
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import plotly.express as px
    import matplotlib.pyplot as plt
    import time
    import koreanize_matplotlib
    
    import folium
    from folium.plugins import MarkerCluster
    import json

    import streamlit as st
    from streamlit_folium import st_folium

    from pyecharts.globals import ThemeType
    from pyecharts.commons.utils import JsCode
    from pyecharts.charts import Bar, Bar3D, Line, Pie, Timeline, Tab
    from pyecharts import options as opts
        

## Data Load
df_korea_city = pd.read_csv("data/korea_city.csv",encoding ='cp949')
df_korea_p_edu = pd.read_csv("data/korea_private-edu.csv",encoding ='cp949')
df_mtoh = pd.read_csv("data/mid_to_high_reason.csv",encoding ='cp949')
df_region_p_edu_type = pd.read_csv('data/region_p_edu_type.csv')
df_region_class_mean = pd.read_csv('data/region_month_pay_p_edu.csv')

## json
g_p = open("data/skorea-municipalities-2018-geo.json", encoding="utf-8")
geo = json.load(g_p)
g_p.close()

## 인트로 
st.markdown("---")
st.markdown("## 프로젝트 배경\n")
st.markdown("##### 1. 초등학교 시험 폐지\n")
st.markdown("2011년 서울을 시작으로 전면 폐지가 되었지만, 수많은 찬반 논란이 존재하고 있다.\n")

st.markdown("##### 2. 학업 성취도의 하락세\n")
st.markdown("학업성취도의 지속적인 하락세와 양극화 현상\n")
st.markdown("\"PISA\" : 학업성취도 국제비교연구로 OECD 각국 교육정책 수립의 기초자료를 제공하기 위해 만 15세 학생을 대상으로 읽기(글 이해력), 수학, 과학 능력을 평가하는 프로그램")
st.markdown("국제 학업 성취도에서 Reading, Math, Science 과목에서 순위가 떨어지고 있는 상황\n")


st.markdown("##### 3.사교육의 확대\n")
st.markdown("사교육 참여 인원은 점점 늘어나고 있지만 학업 성취도는 떨어지고 있는 문제상황에 대한 분석과 해결 방안을 제시\n")

st.markdown("---")
st.markdown("## 데이터 분석 내용")
st.markdown("🗓️시험 폐지 , 자유학기제 시행 이후에도 매년 사교육비 지출은 꾸준히 증가하는 추세이다.\n")

st.markdown("1. 초-중학생 사교육 참여율이 점점 증가하고 있다.\n"
            "2. 전체 학생 평균 사교육비 지출도 점점 커졌다.\n"
            "3. 물가 지수 큰 영향을 미치지는 않았던 것으로 판단된다. \n"
            "4. 이러한 사교육 지출에서 ‘학원’이 가장 큰 비율을 차지했다.\n"
            "5. 서울 강남구에 사설학원이 매우 밀집 되어 있음을 알 수 있었다. \n")
st.markdown("---")
st.markdown("본 프로젝트의 목표는 10년 간 교육 정책에 어떤 변화가 생겼고, 시험 부활에 대한 논의가 \"다시 이루어지게 된 배경\"에 대해 조금 더 자세히 알아보려고 한다.\n")