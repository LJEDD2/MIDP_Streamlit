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

## Title
st.title("λ΄ κ±°μΉ μ±μ κ³Ό λΆμν κ³΅κ΅μ‘~~κ³Όμ~~π¦")

## Header
st.header("π¦ LikeLion AIS7 MID PROJECT")
st.markdown("###### λΆμ μ£Όμ  : μ΄μ€λ± μν νμ§ μ΄ν λνλ―Όκ΅­ μ¬κ΅μ‘ νκ²½ λ³νμ μμΈ λΆμ")
st.markdown("###### νλ‘μ νΈ κΈ°κ° : 2022-10-17 ~ 2022-10-23")
st.markdown(" ")
st.markdown("### π Team Report")
# Link
st.markdown("π GITHUB : [Github LINK ](https://github.com/wumusill/Structure)")
st.markdown("π EDA CODE :[Structure_EDA.ipynb](https://nbviewer.org/github/wumusill/Structure/blob/main/Structure_EDA.ipynb)")
st.markdown("π NOTION: [[κ΅¬μ‘°] MIDνλ‘μ νΈ κ²°κ³Όλ¬Ό](https://canary-beryl-218.notion.site/MiD-9f2b50c7238a4edca1fc07a2dc95f7a9)")
st.markdown("π DASH BOARD : [MIDP_Streamlit.git](https://github.com/LJEDD2/MIDP_Streamlit)")
st.markdown(" ")
st.markdown("## 9οΈβ£ Team Structure ")
st.markdown("""
| κ΅¬μ±μ | μ΄λ¦ | μ­ν  |
| --- | --- | --- |
| π―νμ₯ | μ΄μ μ | μκΈ° (μΌμ  κΈ°λ‘, νμλ‘ μ λ¦¬) , μλ£ μ λ¦¬ λ° μ΄ μ·¨ν© , μμ, κ°μ€ 1 λ°μ΄ν° μμ§ λ° λΆμ (EDA)  λ΄λΉ , Streamlit page μ΄μ κ΅¬μ |
| π¦νμ | κ΅¬μν  | μμ΄λμ΄λ±ν¬ , κ°μ€ 2 λ°μ΄ν° μμ§ λ° λΆμ(EDA) λ΄λΉ, κΉνλΈ Pull Request κ΄λ¦¬ , Streamlit λ² μ΄μ€λΌμΈ μ½λ κ΅¬μΆ   |
| π¦νμ | λ¬Έμ’ν | νμ κΉ νλΈ κ΅μ‘ λ΄λΉ κ°μ€ 3 λ°μ΄ν° μμ§ λ° λΆμ(EDA) λ΄λΉ, κ²°κ³Όλ³΄κ³ μ μμ± λ° μ΅μ’ νμΌ κ²ν , Streamlit λ² μ΄μ€λΌμΈ μ½λ κ΅¬μΆ  |
| π¦νμ | μνμ€ |  PPT μμ± λ° κ²°κ³Ό λ³΄κ³ ν λ°νμ , κ²°κ³Όλ³΄κ³ μ μμ± λ° κ²ν  μμλ¨μ₯, κ°μ€ 4 λ°μ΄ν° μμ§ λ° λΆμ(EDA) λ΄λΉ  |
| π¦νμ | λ¬Έμμ΄  | λ°μ΄ν° μμ§μ μν νλ₯­ν μμμ¬μ , PPT μμ± λ° κ²°κ³Ό λ³΄κ³ ν λ°νμ, κ°μ€ 5 λ°μ΄ν° μμ§ λ° λΆμ(EDA) λ΄λΉ  |

""")
st.markdown("---")
st.markdown("## βν΅μ¬ INSIGHT")
img_4 = Image.open("Result/μ¬λΌμ΄λ15.png")
st.image(img_4,width=1000)
img_1 = Image.open("Result/μ¬λΌμ΄λ8.png")
st.image(img_1,width=1000)
img_2 = Image.open("Result/μ¬λΌμ΄λ11.png")
st.image(img_2,width=1000)
img_3 = Image.open("Result/μ¬λΌμ΄λ12.png")
st.image(img_3,width=1000)

## μΈνΈλ‘ 
st.markdown("---")
st.markdown("## π νλ‘μ νΈ λ°°κ²½\n")
st.markdown("##### 1. μ΄λ±νκ΅ μν νμ§\n")
st.markdown("    - 2011λ μμΈμ μμμΌλ‘ μ λ©΄ νμ§κ° λμμ§λ§, μλ§μ μ°¬λ° λΌλμ΄ μ‘΄μ¬νκ³  μλ€.\n")

st.markdown("##### 2. νμ μ±μ·¨λμ νλ½μΈ\n")
st.markdown("    - νμμ±μ·¨λμ μ§μμ μΈ νλ½μΈμ μκ·Ήν νμ\n")
st.markdown("    - \"PISA\" : νμμ±μ·¨λ κ΅­μ λΉκ΅μ°κ΅¬λ‘ OECD κ°κ΅­ κ΅μ‘μ μ± μλ¦½μ κΈ°μ΄μλ£λ₯Ό μ κ³΅νκΈ° μν΄ λ§ 15μΈ νμμ λμμΌλ‘ μ½κΈ°(κΈ μ΄ν΄λ ₯), μν, κ³Όν λ₯λ ₯μ νκ°νλ νλ‘κ·Έλ¨")
st.markdown("    - κ΅­μ  νμ μ±μ·¨λμμ Reading, Math, Science κ³Όλͺ©μμ μμκ° λ¨μ΄μ§κ³  μλ μν©\n")


st.markdown("##### 3. μ¬κ΅μ‘μ νλ\n")
st.markdown("    - μ¬κ΅μ‘ μ°Έμ¬ μΈμμ μ μ  λμ΄λκ³  μμ§λ§ νμ μ±μ·¨λλ λ¨μ΄μ§κ³  μλ λ¬Έμ μν©μ λν λΆμκ³Ό ν΄κ²° λ°©μμ μ μ\n")

st.markdown("---")
st.markdown("## π Hypothesis ")
st.markdown("ποΈ μν νμ§ , μμ νκΈ°μ  μν μ΄νμλ λ§€λ μ¬κ΅μ‘λΉ μ§μΆμ κΎΈμ€ν μ¦κ°νλ μΆμΈμ΄λ€.\n")
st.markdown("μνμ΄ νμ§λ μ΄ν 10λ κ° λνλ―Όκ΅­μ κ΅μ‘ μ μ±μ μ΄λ€ λ³νκ° μκ²Όλμ§,\n\n κ·Έλ¦¬κ³  νμ¬ μν λΆνμ λν λΌμκ° λ€μ μ΄λ£¨μ΄μ§κ² λ λ°°κ²½μ λν΄ μ‘°κΈ λ μμΈν μμλ³΄κ³ μ νλ€. \n")

st.markdown("1. μ΄-μ€νμ μ¬κ΅μ‘ μ°Έμ¬μ¨μ΄ μ μ  μ¦κ°νκ³  μλ€.\n"
            "2. μλ₯κ³Ό κ΄λ ¨λ κ΅κ³Όλͺ©μ μ€μ μΌλ‘ μ¬κ΅μ‘μ λ³νν  κ²μ΄λ€.\n"
            "3. νμ λ° λ³΄μ΅ κ΅μ‘ λ¬Όκ°μ§μμλ ν° μν₯μ λ―Έμ³€μ κ²μ΄λ€.  \n"
            "4. μ¬κ΅μ‘μ βμ¬μ€νμβμμ κ°μ₯ λ§μ΄ μ΄λ£¨μ΄μ§κ³  μμ κ²μ΄λ€.\n"
            "5. μ²­μλλ€μ΄ μ μ  νμμ ν₯λ―Έλ₯Ό μμ΄κ°κ³  μμΌλ©°, νμ μ±μ·¨λ λν νλ½μΈμΌ κ²μ΄λ€.\n"
            "6. μ½λ‘λ μ΄ν νμμ μ€λ¨νλ μ²­μλλ€μ΄ λμ΄λ¬μ κ²μ΄λ€. \n")



st.markdown("---")
st.markdown("## π₯ Dataset ")
st.markdown("π [μ§μ­λ³ 1μΈλΉ μνκ·  μ¬κ΅μ‘λΉ μ§μΆ νν© (2011 ~ 2022)](https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1PE202&vw_cd=MT_ZTITLE&list_id=H1_10_005&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE)")
st.markdown("π [κ° νκ΅κΈ κ³Όλͺ©λ³ 1μΈλΉ μ νκ·  μ¬κ΅μ‘λΉ μ§μΆ νν©  ](https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1PE202&vw_cd=MT_ZTITLE&list_id=H1_10_005&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE)  ")
st.markdown("π [μμΈμ μ¬μ€νμ ν΅κ³(μ°λ/ κ΅¬λ³/ μ¬μ€νμ (νκ΅κ΅κ³Όκ΅μ΅νμ))](https://data.seoul.go.kr/dataList/195/S/2/datasetView.do)  ")
st.markdown("π [νμμ±μ·¨λ νκ°(κ΅κ³Όλ³ μ±μ·¨μμ€ λΉμ¨)](https://www.index.go.kr/potal/main/EachDtlPageDetail.do?idx_cd=1539) ")
st.markdown("π [κ΅­μ νμμ±μ·¨λνκ°(PISA)](https://www.index.go.kr/potal/main/EachDtlPageDetail.do?idx_cd=1539) ")
st.markdown("π [μ€κ³ λ±νμ νμμ±μ·¨ μ§νμ§](https://naea.kice.re.kr/prtl/rept/info/rate-year) ")
st.markdown("π [μμΈμ νμμ νκ΅μν λ§μ‘±λ ν΅κ³](https://data.seoul.go.kr/dataList/10779/S/2/datasetView.do) ")
st.markdown("π [μκ²©μμ μ¬λΆβ€ν¨κ³Όμ± μ¬λΆ λ° λΉν¨μ¨μ μΈ μ΄μ  (μ£Όλμλ΅, 18μΈ μ΄ν μΈκ΅¬)](https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1SSCV061R&vw_cd=MT_ZTITLE&list_id=B_7_D220&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE) ")
st.markdown("π [μμΈμ νμμ±μ·¨μμ€ λΉμ¨ ν΅κ³](https://data.seoul.go.kr/dataList/10768/C/2/datasetView.do) ")
st.markdown("π [2011~20λ μμΈμ μμΉκ΅¬λ³ μ΄μ€κ³  νμμ€λ¨λ₯  ](https://data.seoul.go.kr/dataList/10713/C/2/datasetView.do) ")
st.markdown("π [μμΈμ μ νμ νν© ν΅κ³(12~20λ)](https://data.seoul.go.kr/dataList/10802/C/2/datasetView.do;jsessionid=B2362306095F4A8304B584194340C61E.new_portal-svr-21) ")
st.markdown("π [etc](https://www.notion.so/MiD-9f2b50c7238a4edca1fc07a2dc95f7a9#903d1302da864db590d37bc9c3b73a8a)")
st.markdown("---")

st.markdown("## ποΈ Library")
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
    