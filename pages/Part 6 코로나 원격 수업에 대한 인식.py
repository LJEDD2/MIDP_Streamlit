import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
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


raw = pd.read_csv("data/online_satisfaction.csv", encoding="cp949")

col = raw.iloc[0,:].str.strip()
raw.columns = col
raw = raw.drop([0,1]).reset_index(drop=True)
raw["항목"] = raw["항목"].str.replace("[-?]", "", regex=True).str.strip()
df_online = pd.melt(raw, id_vars=["항목","계"], value_vars=col[6:8], var_name="성별", value_name="비율")
df_online["계"] = pd.to_numeric(df_online["계"], errors="coerce")
df_online["비율"] = pd.to_numeric(df_online["비율"], errors="coerce")
df_online_per = df_online.loc[df_online["항목"].str.contains("원격수업함|원격수업 안함"), ["항목", "계"]]
df_online_per = df_online_per[df_online_per.duplicated()]

df_effect = df_online[df_online["항목"].str.contains("원격수업  효과적이었음|원격수업  효과적이지 않았음")]
df_effect2 = df_effect[df_effect[["항목","계"]].duplicated()]

df_reason = df_online[~df_online["항목"].str.contains("원격수업함|원격수업  효과적이었음|원격수업  효과적이지 않았음|기타|원격수업 안함")]
df_reason = df_reason[df_reason[["항목","계"]].duplicated()]
df_reason = df_reason.sort_values(by="계",ascending=True)

colors = sns.color_palette("pastel", 2).as_hex()
colors2 = sns.color_palette("pastel", 8).as_hex()

st.header("6️⃣ Part 6 : 코로나 이후 온라인 학습에 대한 인식")
st.markdown("코로나 사태 이후 청소년들의 온라인 학습에 대한 인식 조사")
st.markdown("---")

st.markdown("### 🙋‍♀️코로나 이후 학생 중 온라인 학습을 얼마나 경험했나요?")
if st.checkbox('Show Code',key=11):
    with st.echo():
        fig1 = px.pie(df_online_per, values="계", names="항목", title="온라인 학습 경험 비율(2021년 기준), %")
        

fig1 = px.pie(df_online_per, values="계", names="항목", title="온라인 학습 경험 비율(2021년 기준 :%)")
st.plotly_chart(fig1)
st.markdown("---")

st.markdown("### 🙋‍♂️온라인 수업이 효과적이지 않다고 생각하나요?")
if st.checkbox('Show Code',key=12):
    with st.echo():
        data2 = go.Bar(x=df_effect2["항목"], y=df_effect2["계"], marker = {'color':colors, # 막대 색상 또는 리스트를 이용하여 각 막대 색상 변경가능
                                    'line':{'color':'black', 'width':3}, # 막대 테두리 설정
                                    'pattern':{'shape':'/'}, # 사선 패턴
                                    },
              width=0.5,)

        layout2 = go.Layout(title='원격수업 효과성 판단 여부, %', font={'size':15})              
        fig2 = go.Figure(data=data2, layout=layout2)
       

data2 = go.Bar(x=df_effect2["항목"], y=df_effect2["계"], marker = {'color':colors, # 막대 색상 또는 리스트를 이용하여 각 막대 색상 변경가능
                                    'line':{'color':'black', 'width':3}, # 막대 테두리 설정
                                    'pattern':{'shape':'/'}, # 사선 패턴
                                    },
              width=0.5,)

layout2 = go.Layout(title='원격수업 효과성 판단 여부(%)', font={'size':15})              
fig2 = go.Figure(data=data2, layout=layout2)
st.plotly_chart(fig2)

st.markdown("---")
st.markdown("### 🙋온라인 수업이 효과적이지 않았다면 그 이유는 무엇인가요?")
if st.checkbox('Show Code',key=13):
    with st.echo():
        data3 = go.Bar(x=df_reason["계"], y=df_reason["항목"], 
                        orientation='h', marker = {'color':colors2, # 막대 색상 또는 리스트를 이용하여 각 막대 색상 변경가능
                                            'line':{'color':'black', 'width':3}, # 막대 테두리 설정
                                            'pattern':{'shape':'/'}, # 사선 패턴
                                            },
                                            width=0.5)

        layout3 = go.Layout(title='원격수업 불만족 이유, %', font={'size':15})              
        fig3 = go.Figure(data=data3, layout=layout3)
        fig3.update_layout(autosize=False,
            width=1000,
            height=1000)
        

data3 = go.Bar(x=df_reason["계"], y=df_reason["항목"], 
                orientation='h', marker = {'color':colors2, # 막대 색상 또는 리스트를 이용하여 각 막대 색상 변경가능
                                    'line':{'color':'black', 'width':3}, # 막대 테두리 설정
                                    'pattern':{'shape':'/'}, # 사선 패턴
                                    },
                                    width=0.5)

layout3 = go.Layout(title='원격수업 불만족 이유(%)', font={'size':15})              
fig3 = go.Figure(data=data3, layout=layout3)
fig3.update_layout(autosize=False,
    width=1000,
    height=1000)
st.plotly_chart(fig3)

