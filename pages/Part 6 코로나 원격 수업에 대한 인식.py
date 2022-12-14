import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
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


raw = pd.read_csv("data/online_satisfaction.csv", encoding="cp949")

col = raw.iloc[0,:].str.strip()
raw.columns = col
raw = raw.drop([0,1]).reset_index(drop=True)
raw["ν­λͺ©"] = raw["ν­λͺ©"].str.replace("[-?]", "", regex=True).str.strip()
df_online = pd.melt(raw, id_vars=["ν­λͺ©","κ³"], value_vars=col[6:8], var_name="μ±λ³", value_name="λΉμ¨")
df_online["κ³"] = pd.to_numeric(df_online["κ³"], errors="coerce")
df_online["λΉμ¨"] = pd.to_numeric(df_online["λΉμ¨"], errors="coerce")
df_online_per = df_online.loc[df_online["ν­λͺ©"].str.contains("μκ²©μμν¨|μκ²©μμ μν¨"), ["ν­λͺ©", "κ³"]]
df_online_per = df_online_per[df_online_per.duplicated()]

df_effect = df_online[df_online["ν­λͺ©"].str.contains("μκ²©μμ  ν¨κ³Όμ μ΄μμ|μκ²©μμ  ν¨κ³Όμ μ΄μ§ μμμ")]
df_effect2 = df_effect[df_effect[["ν­λͺ©","κ³"]].duplicated()]

df_reason = df_online[~df_online["ν­λͺ©"].str.contains("μκ²©μμν¨|μκ²©μμ  ν¨κ³Όμ μ΄μμ|μκ²©μμ  ν¨κ³Όμ μ΄μ§ μμμ|κΈ°ν|μκ²©μμ μν¨")]
df_reason = df_reason[df_reason[["ν­λͺ©","κ³"]].duplicated()]
df_reason = df_reason.sort_values(by="κ³",ascending=True)

colors = sns.color_palette("pastel", 2).as_hex()
colors2 = sns.color_palette("pastel", 8).as_hex()

st.header("6οΈβ£ Part 6 : μ½λ‘λ μ΄ν μ¨λΌμΈ νμ΅μ λν μΈμ")
st.markdown("μ½λ‘λ μ¬ν μ΄ν μ²­μλλ€μ μ¨λΌμΈ νμ΅μ λν μΈμ μ‘°μ¬")
st.markdown("---")

st.markdown("### πββοΈμ½λ‘λ μ΄ν νμ μ€ μ¨λΌμΈ νμ΅μ μΌλ§λ κ²½ννλμ?")
if st.checkbox('Show Code',key=11):
    with st.echo():
        fig1 = px.pie(df_online_per, values="κ³", names="ν­λͺ©", title="μ¨λΌμΈ νμ΅ κ²½ν λΉμ¨(2021λ κΈ°μ€), %")
        

fig1 = px.pie(df_online_per, values="κ³", names="ν­λͺ©", title="μ¨λΌμΈ νμ΅ κ²½ν λΉμ¨(2021λ κΈ°μ€ :%)")
st.plotly_chart(fig1)
st.markdown("---")

st.markdown("### πββοΈμ¨λΌμΈ μμμ΄ ν¨κ³Όμ μ΄μ§ μλ€κ³  μκ°νλμ?")
if st.checkbox('Show Code',key=12):
    with st.echo():
        data2 = go.Bar(x=df_effect2["ν­λͺ©"], y=df_effect2["κ³"], marker = {'color':colors, # λ§λ μμ λλ λ¦¬μ€νΈλ₯Ό μ΄μ©νμ¬ κ° λ§λ μμ λ³κ²½κ°λ₯
                                    'line':{'color':'black', 'width':3}, # λ§λ νλλ¦¬ μ€μ 
                                    'pattern':{'shape':'/'}, # μ¬μ  ν¨ν΄
                                    },
              width=0.5,)

        layout2 = go.Layout(title='μκ²©μμ ν¨κ³Όμ± νλ¨ μ¬λΆ, %', font={'size':15})              
        fig2 = go.Figure(data=data2, layout=layout2)
       

data2 = go.Bar(x=df_effect2["ν­λͺ©"], y=df_effect2["κ³"], marker = {'color':colors, # λ§λ μμ λλ λ¦¬μ€νΈλ₯Ό μ΄μ©νμ¬ κ° λ§λ μμ λ³κ²½κ°λ₯
                                    'line':{'color':'black', 'width':3}, # λ§λ νλλ¦¬ μ€μ 
                                    'pattern':{'shape':'/'}, # μ¬μ  ν¨ν΄
                                    },
              width=0.5,)

layout2 = go.Layout(title='μκ²©μμ ν¨κ³Όμ± νλ¨ μ¬λΆ(%)', font={'size':15})              
fig2 = go.Figure(data=data2, layout=layout2)
st.plotly_chart(fig2)

st.markdown("---")
st.markdown("### πμ¨λΌμΈ μμμ΄ ν¨κ³Όμ μ΄μ§ μμλ€λ©΄ κ·Έ μ΄μ λ λ¬΄μμΈκ°μ?")
if st.checkbox('Show Code',key=13):
    with st.echo():
        data3 = go.Bar(x=df_reason["κ³"], y=df_reason["ν­λͺ©"], 
                        orientation='h', marker = {'color':colors2, # λ§λ μμ λλ λ¦¬μ€νΈλ₯Ό μ΄μ©νμ¬ κ° λ§λ μμ λ³κ²½κ°λ₯
                                            'line':{'color':'black', 'width':3}, # λ§λ νλλ¦¬ μ€μ 
                                            'pattern':{'shape':'/'}, # μ¬μ  ν¨ν΄
                                            },
                                            width=0.5)

        layout3 = go.Layout(title='μκ²©μμ λΆλ§μ‘± μ΄μ , %', font={'size':15})              
        fig3 = go.Figure(data=data3, layout=layout3)
        fig3.update_layout(autosize=False,
            width=1000,
            height=1000)
        

data3 = go.Bar(x=df_reason["κ³"], y=df_reason["ν­λͺ©"], 
                orientation='h', marker = {'color':colors2, # λ§λ μμ λλ λ¦¬μ€νΈλ₯Ό μ΄μ©νμ¬ κ° λ§λ μμ λ³κ²½κ°λ₯
                                    'line':{'color':'black', 'width':3}, # λ§λ νλλ¦¬ μ€μ 
                                    'pattern':{'shape':'/'}, # μ¬μ  ν¨ν΄
                                    },
                                    width=0.5)

layout3 = go.Layout(title='μκ²©μμ λΆλ§μ‘± μ΄μ (%)', font={'size':15})              
fig3 = go.Figure(data=data3, layout=layout3)
fig3.update_layout(autosize=False,
    width=1000,
    height=1000)
st.plotly_chart(fig3)

