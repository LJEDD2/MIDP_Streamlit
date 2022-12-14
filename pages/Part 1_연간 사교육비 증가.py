import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit as st
import time
import koreanize_matplotlib
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="9์กฐ streamlit_page",
    page_icon="๐",
    layout="wide",
) # ์นํ์ด์ง ํญ ๋์์ธ ์ค์ 

# ํ์ด์ง ๋ก๋ ์งํ ์ํฉ ๋ฐ
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

## part 1
# ํ๊ต๊ธ ์ฌ๊ต์ก ์ฐธ์ฌ์จ ๋น๊ต 
df_participation_ratio = pd.read_csv('data/region_subject_ratio.csv',encoding='cp949',index_col=0)

st.header("1๏ธโฃ Part 1 : ์ง์ญ๋ณ ์ฌ๊ต์ก ์ฐธ์ฌ์จ ๋ณํ")
st.markdown("## ๐ข Dataset ")
st.dataframe(df_participation_ratio)
st.markdown("---")
st.markdown("### ๐ถ ๊ฐ ์ง์ญ์ ๊ณผ๋ชฉ๋ณ ์ฌ๊ต์ก ์ฐธ์ฌ์จ ๋ฐ ์ ํ๊ท  ์ง์ถ๋น์ฉ ๋น๊ต")
HtmlFile_regratio = open("data/df_region_subject_chart.html", 'r', encoding='utf-8')
source_code_regratio = HtmlFile_regratio.read() 
print(source_code_regratio)
components.html(source_code_regratio,height=600)

## part 2 
# ์ฐ๊ฐ 1์ธ๋น ์ ํ๊ท  ์ฌ๊ต์ก๋น ์ง์ถ์ ๋ณํ๋ฅผ ์ง์ญ-ํ๊ต๊ธ-๊ณผ๋ชฉ๋ณ๋ก ๋ถ์ 
 
# ์ฌ๊ต์ก๋น ๋ฐ์ดํฐ ๋ก๋
@st.cache(allow_output_mutation=True)
def load_private_data():
    data = pd.read_csv("https://raw.githubusercontent.com/wumusill/Structure/main/dataset/seoul_private.csv")
    data = data.drop([0, 1, 2])
    return data

st.markdown("### ๐ถ ์์ธ์์ 1์ธ๋น ์ํ๊ท  ์ง์ถ ์ฌ๊ต์ก๋น ๋น๊ต (๋จ์ :๋ง์)")
private_data = load_private_data()
private_data.columns = ["์์ ", "ํ๊ท  ์ฌ๊ต์ก๋น", "ํ๊ท  ์ฌ๊ต์ก ์ฐธ์ฌ์จ(%)", 
                    "์ด๋ฑํ๊ต ์ฌ๊ต์ก๋น", "์ด๋ฑ ์ฌ๊ต์ก ์ฐธ์ฌ์จ(%)", 
                    "์คํ๊ต ์ฌ๊ต์ก๋น", "์ค๋ฑ ์ฌ๊ต์ก ์ฐธ์ฌ์จ(%)", 
                    "๊ณ ๋ฑํ๊ต ์ฌ๊ต์ก๋น", "๊ณ ๋ฑ ์ฌ๊ต์ก ์ฐธ์ฌ์จ(%)", 
                    "์ผ๋ฐ๊ณ  ์ฌ๊ต์ก๋น", "์ผ๋ฐ๊ณ  ์ฌ๊ต์ก ์ฐธ์ฌ์จ(%)"]
private_data = private_data.astype('float')

condition = private_data.columns.str.contains("์ฌ๊ต์ก๋น")
ratio_df = private_data.loc[:, ~condition]
ratio_df.index = ["11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"]

cost_df = private_data.loc[:, condition]
cost_df.index = ["11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"]



# 1์ธ๋น ํ๊ท  ์ฌ๊ต์ก๋น ๊ทธ๋ํ
if st.checkbox('Show Code'):
    with st.echo():
        plt.set_loglevel('WARNING')
        fig1 = plt.figure(figsize=(10, 5))
        sns.lineplot(data=cost_df, x=cost_df.index, y="ํ๊ท  ์ฌ๊ต์ก๋น", label="ํ๊ท ")
        sns.lineplot(data=cost_df, x=cost_df.index, y="์ด๋ฑํ๊ต ์ฌ๊ต์ก๋น", label="์ด๋ฑํ๊ต")
        sns.lineplot(data=cost_df, x=cost_df.index, y="์คํ๊ต ์ฌ๊ต์ก๋น", label="์คํ๊ต")
        sns.lineplot(data=cost_df, x=cost_df.index, y="๊ณ ๋ฑํ๊ต ์ฌ๊ต์ก๋น", label="๊ณ ๋ฑํ๊ต")
        sns.lineplot(data=cost_df, x=cost_df.index, y="์ผ๋ฐ๊ณ  ์ฌ๊ต์ก๋น", label="์ผ๋ฐ๊ณ ")
        plt.legend(bbox_to_anchor=(1, 1))
        plt.title("1์ธ๋น ํ๊ท  ์ฌ๊ต์ก๋น (๋ง์)")
        plt.axvline(x = '15',linestyle='--')
        plt.axvline(x = '19',linestyle='--')

        # ์ฌ๊ต์ก ์ฐธ์ฌ์จ ๊ทธ๋ํ
        fig2 = plt.figure(figsize=(10, 5))
        sns.lineplot(data=ratio_df, x=ratio_df.index, y="ํ๊ท  ์ฌ๊ต์ก ์ฐธ์ฌ์จ(%)", label="ํ๊ท ")
        sns.lineplot(data=ratio_df, x=ratio_df.index, y="์ด๋ฑ ์ฌ๊ต์ก ์ฐธ์ฌ์จ(%)", label="์ด๋ฑ")
        sns.lineplot(data=ratio_df, x=ratio_df.index, y="์ค๋ฑ ์ฌ๊ต์ก ์ฐธ์ฌ์จ(%)", label="์ค๋ฑ")
        sns.lineplot(data=ratio_df, x=ratio_df.index, y="๊ณ ๋ฑ ์ฌ๊ต์ก ์ฐธ์ฌ์จ(%)", label="๊ณ ๋ฑ")
        sns.lineplot(data=ratio_df, x=ratio_df.index, y="์ผ๋ฐ๊ณ  ์ฌ๊ต์ก ์ฐธ์ฌ์จ(%)", label="์ผ๋ฐ๊ณ ")
        plt.legend(bbox_to_anchor=(1, 1))
        plt.title("์ฌ๊ต์ก ์ฐธ์ฌ์จ (%)")
        plt.axvline(x = '15',linestyle='--')
        plt.axvline(x = '19',linestyle='--')# Layout

plt.set_loglevel('WARNING')
fig1 = plt.figure(figsize=(10, 5))
sns.lineplot(data=cost_df, x=cost_df.index, y="ํ๊ท  ์ฌ๊ต์ก๋น", label="ํ๊ท ")
sns.lineplot(data=cost_df, x=cost_df.index, y="์ด๋ฑํ๊ต ์ฌ๊ต์ก๋น", label="์ด๋ฑํ๊ต")
sns.lineplot(data=cost_df, x=cost_df.index, y="์คํ๊ต ์ฌ๊ต์ก๋น", label="์คํ๊ต")
sns.lineplot(data=cost_df, x=cost_df.index, y="๊ณ ๋ฑํ๊ต ์ฌ๊ต์ก๋น", label="๊ณ ๋ฑํ๊ต")
sns.lineplot(data=cost_df, x=cost_df.index, y="์ผ๋ฐ๊ณ  ์ฌ๊ต์ก๋น", label="์ผ๋ฐ๊ณ ")
plt.legend(bbox_to_anchor=(1, 1))
plt.title("1์ธ๋น ํ๊ท  ์ฌ๊ต์ก๋น (๋ง์)")
plt.axvline(x = '15',linestyle='--')
plt.axvline(x = '19',linestyle='--')

# ์ฌ๊ต์ก ์ฐธ์ฌ์จ ๊ทธ๋ํ
fig2 = plt.figure(figsize=(10, 5))
sns.lineplot(data=ratio_df, x=ratio_df.index, y="ํ๊ท  ์ฌ๊ต์ก ์ฐธ์ฌ์จ(%)", label="ํ๊ท ")
sns.lineplot(data=ratio_df, x=ratio_df.index, y="์ด๋ฑ ์ฌ๊ต์ก ์ฐธ์ฌ์จ(%)", label="์ด๋ฑ")
sns.lineplot(data=ratio_df, x=ratio_df.index, y="์ค๋ฑ ์ฌ๊ต์ก ์ฐธ์ฌ์จ(%)", label="์ค๋ฑ")
sns.lineplot(data=ratio_df, x=ratio_df.index, y="๊ณ ๋ฑ ์ฌ๊ต์ก ์ฐธ์ฌ์จ(%)", label="๊ณ ๋ฑ")
sns.lineplot(data=ratio_df, x=ratio_df.index, y="์ผ๋ฐ๊ณ  ์ฌ๊ต์ก ์ฐธ์ฌ์จ(%)", label="์ผ๋ฐ๊ณ ")
plt.legend(bbox_to_anchor=(1, 1))
plt.title("์ฌ๊ต์ก ์ฐธ์ฌ์จ (%)")
plt.axvline(x = '15',linestyle='--')
plt.axvline(x = '19',linestyle='--')# Layout
        
container1 = st.container()
col1, col2 = st.columns(2)

with container1:
    with col1:
        fig1
    with col2:
        fig2
