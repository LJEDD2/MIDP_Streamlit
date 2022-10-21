import streamlit as st
import streamlit.components.v1 as components

# >>> import plotly.express as px
# >>> fig = px.box(range(10))
# >>> fig.write_html('test.html')

st.header("Part 3 : 학업성취도와 학업 인식 수준 변화")

st.markdown("### 📶중-고등학생의 진학 학교 및 진로 선택 기준")
HtmlFile_2 = open("data/df_korea_student.html", 'r', encoding='utf-8')
source_code_2 = HtmlFile_2.read() 
print(source_code_2)
components.html(source_code_2,height=500)

st.markdown("### 📶학교급별 희망하는 직업 유무와 희망하는 최종 학력 수준")
HtmlFile_1 = open("data/df_survey_by_school_level.html", 'r', encoding='utf-8')
source_code_1 = HtmlFile_1.read() 
print(source_code_1)
components.html(source_code_1,height=800)
