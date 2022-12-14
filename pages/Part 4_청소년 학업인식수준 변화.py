import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
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

st.header("4οΈβ£ Part 4 : μ²­μλ νμ μΈμ μμ€ λ³ν")
st.markdown("μ€-κ³ λ±νμμ μ§ν μ§λ‘ μ ν κΈ°μ€μ λ³νμ ν¬λ§νλ μ§μμ μ λ¬΄, ν¬λ§νλ μ΅μ’ νλ ₯ μμ€μ λν΄ λΆμ")
st.markdown("---")
st.markdown("### πΆμ€-κ³ λ±νμμ μ§ν νκ΅ λ° μ§λ‘ μ ν κΈ°μ€")

HtmlFile_2 = open("data/df_korea_student.html", 'r', encoding='utf-8')
source_code_2 = HtmlFile_2.read() 
print(source_code_2)
components.html(source_code_2,height=500)
st.markdown("---")
st.markdown("### πΆνκ΅κΈλ³ ν¬λ§νλ μ§μ μ λ¬΄μ ν¬λ§νλ μ΅μ’ νλ ₯ μμ€")
HtmlFile_1 = open("data/df_survey_by_school_level.html", 'r', encoding='utf-8')
source_code_1 = HtmlFile_1.read() 
print(source_code_1)
components.html(source_code_1,height=800)

