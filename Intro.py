import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import folium
import json
from PIL import Image

import streamlit as st
from streamlit_folium import st_folium
import time
import koreanize_matplotlib
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Bar, Bar3D, Line, Pie, Timeline, Tab
from pyecharts import options as opts

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

## Title
st.title("내 거친 성적과 불안한 공교육~~과악~~💦")

## Header
st.header("🦁 LikeLion AIS7 MID PROJECT")
st.markdown("###### 분석 주제 : 초중등 시험 폐지 이후 대한민국 사교육 환경 변화와 원인 분석")
st.markdown("###### 프로젝트 기간 : 2022-10-17 ~ 2022-10-23")
st.markdown(" ")
st.markdown("### 📈 Team Report")
# Link
st.markdown("🔗 GITHUB : [Github LINK ](https://github.com/wumusill/Structure)")
st.markdown("🔗 EDA CODE :[Structure_EDA.ipynb](https://nbviewer.org/github/LJEDD2/Structure/blob/main/Structure_EDA.ipynb)")
st.markdown("🔗 NOTION: [[구조] MID프로젝트 결과물](https://canary-beryl-218.notion.site/MiD-9f2b50c7238a4edca1fc07a2dc95f7a9)")
st.markdown("🔗 DASH BOARD : [MIDP_Streamlit.git](https://github.com/LJEDD2/MIDP_Streamlit)")
st.markdown(" ")
st.markdown("## 9️⃣ Team Structure ")
st.markdown("""
| 구성원 | 이름 | 역할 |
| --- | --- | --- |
| 🐯팀장 | 이정은 | 서기 (일정 기록, 회의록 정리) , 자료 정리 및 총 취합 , 응원, 가설 1 데이터 수집 및 분석 (EDA)  담당 , Streamlit page 초안 구상 |
| 🦁팀원 | 구자현  | 아이디어뱅크 , 가설 2 데이터 수집 및 분석(EDA) 담당, 깃허브 Pull Request 관리 , Streamlit 베이스라인 코드 구축   |
| 🦁팀원 | 문종현 | 팀원 깃 허브 교육 담당 가설 3 데이터 수집 및 분석(EDA) 담당, 결과보고서 작성 및 최종 파일 검토, Streamlit 베이스라인 코드 구축  |
| 🦁팀원 | 안혜윤 |  PPT 작성 및 결과 보고회 발표자 , 결과보고서 작성 및 검토 응원단장, 가설 4 데이터 수집 및 분석(EDA) 담당  |
| 🦁팀원 | 문영운  | 데이터 수집을 위한 훌륭한 영업사원 , PPT 작성 및 결과 보고회 발표자, 가설 5 데이터 수집 및 분석(EDA) 담당  |

""")
st.markdown("---")
st.markdown("## ❓핵심 INSIGHT")
img_4 = Image.open("Result/슬라이드15.png")
st.image(img_4,width=1000)
img_1 = Image.open("Result/슬라이드8.png")
st.image(img_1,width=1000)
img_2 = Image.open("Result/슬라이드11.png")
st.image(img_2,width=1000)
img_3 = Image.open("Result/슬라이드12.png")
st.image(img_3,width=1000)

## 인트로 
st.markdown("---")
st.markdown("## 📑 프로젝트 배경\n")
st.markdown("##### 1. 초등학교 시험 폐지\n")
st.markdown("    - 2011년 서울을 시작으로 전면 폐지가 되었지만, 수많은 찬반 논란이 존재하고 있다.\n")

st.markdown("##### 2. 학업 성취도의 하락세\n")
st.markdown("    - 학업성취도의 지속적인 하락세와 양극화 현상\n")
st.markdown("    - \"PISA\" : 학업성취도 국제비교연구로 OECD 각국 교육정책 수립의 기초자료를 제공하기 위해 만 15세 학생을 대상으로 읽기(글 이해력), 수학, 과학 능력을 평가하는 프로그램")
st.markdown("    - 국제 학업 성취도에서 Reading, Math, Science 과목에서 순위가 떨어지고 있는 상황\n")


st.markdown("##### 3. 사교육의 확대\n")
st.markdown("    - 사교육 참여 인원은 점점 늘어나고 있지만 학업 성취도는 떨어지고 있는 문제상황에 대한 분석과 해결 방안을 제시\n")

st.markdown("---")
st.markdown("## 📝 Hypothesis ")
st.markdown("🗓️ 시험 폐지 , 자유학기제 시행 이후에도 매년 사교육비 지출은 꾸준히 증가하는 추세이다.\n")
st.markdown("시험이 폐지된 이후 10년 간 대한민국의 교육 정책에 어떤 변화가 생겼는지,\n\n 그리고 현재 시험 부활에 대한 논의가 다시 이루어지게 된 배경에 대해 조금 더 자세히 알아보고자 한다. \n")

st.markdown("1. 초-중학생 사교육 참여율이 점점 증가하고 있다.\n"
            "2. 수능과 관련된 교과목을 중점으로 사교육을 병행할 것이다.\n"
            "3. 학원 및 보습 교육 물가지수에는 큰 영향을 미쳤을 것이다.  \n"
            "4. 사교육은 ‘사설학원’에서 가장 많이 이루어지고 있을 것이다.\n"
            "5. 청소년들이 점점 학업에 흥미를 잃어가고 있으며, 학업 성취도 또한 하락세일 것이다.\n"
            "6. 코로나 이후 학업을 중단하는 청소년들이 늘어났을 것이다. \n")



st.markdown("---")
st.markdown("## 📥 Dataset ")
st.markdown("🔗 [지역별 1인당 월평균 사교육비 지출 현황 (2011 ~ 2022)](https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1PE202&vw_cd=MT_ZTITLE&list_id=H1_10_005&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE)")
st.markdown("🔗 [각 학교급 과목별 1인당 월 평균 사교육비 지출 현황  ](https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1PE202&vw_cd=MT_ZTITLE&list_id=H1_10_005&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE)  ")
st.markdown("🔗 [서울시 사설학원 통계(연도/ 구별/ 사설학원 (학교교과교습학원))](https://data.seoul.go.kr/dataList/195/S/2/datasetView.do)  ")
st.markdown("🔗 [학업성취도 평가(교과별 성취수준 비율)](https://www.index.go.kr/potal/main/EachDtlPageDetail.do?idx_cd=1539) ")
st.markdown("🔗 [국제학업성취도평가(PISA)](https://www.index.go.kr/potal/main/EachDtlPageDetail.do?idx_cd=1539) ")
st.markdown("🔗 [중고등학생 학업성취 지표집](https://naea.kice.re.kr/prtl/rept/info/rate-year) ")
st.markdown("🔗 [서울시 학생의 학교생활 만족도 통계](https://data.seoul.go.kr/dataList/10779/S/2/datasetView.do) ")
st.markdown("🔗 [원격수업 여부․효과성 여부 및 비효율적인 이유 (주된응답, 18세 이하 인구)](https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1SSCV061R&vw_cd=MT_ZTITLE&list_id=B_7_D220&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE) ")
st.markdown("🔗 [서울시 학업성취수준 비율 통계](https://data.seoul.go.kr/dataList/10768/C/2/datasetView.do) ")
st.markdown("🔗 [2011~20년 서울시 자치구별 초중고 학업중단률 ](https://data.seoul.go.kr/dataList/10713/C/2/datasetView.do) ")
st.markdown("🔗 [서울시 유학생 현황 통계(12~20년)](https://data.seoul.go.kr/dataList/10802/C/2/datasetView.do;jsessionid=B2362306095F4A8304B584194340C61E.new_portal-svr-21) ")
st.markdown("🔗 [etc](https://www.notion.so/MiD-9f2b50c7238a4edca1fc07a2dc95f7a9#903d1302da864db590d37bc9c3b73a8a)")
st.markdown("---")

st.markdown("## 🗃️ Library")
with st.echo():
    import sys
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import koreanize_matplotlib
    import matplotlib.pyplot as plt

    from glob import glob
    from PIL import Image

    import datetime as dt
    from dateutil.parser import parse

    import FinanceDataReader as fdr
    import plotly.express as px
    import plotly.graph_objects as go

    import matplotlib.font_manager as fm
    import requests
    import warnings
    import folium
    import json
    