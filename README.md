# 🦁 LikeLion AIS7 MID PROJECT 
- 멋쟁이 사자처럼 미드프로젝트 공공데이터 수집 및 EDA
- 대시보드 시각화
---
## 내 거친 성적과 불안한 공교육~~과악~~💦 
###### 분석 주제 : 초중등 시험 폐지 이후 대한민국 사교육 환경 변화와 원인 분석
###### 프로젝트 기간 : 2022-10-17 ~ 2022-10-23

### 📈 Team Report

🔽LINK  
🔗 GITHUB : [Github LINK ](https://github.com/wumusill/Structure)  
🔗 EDA CODE :[Structure_EDA.ipynb](https://nbviewer.org/github/LJEDD2/Structure/blob/main/Structure_EDA.ipynb)  
🔗 NOTION: [[구조] MID프로젝트 결과물](https://canary-beryl-218.notion.site/MiD-9f2b50c7238a4edca1fc07a2dc95f7a9)  
🔗 DASH BOARD : [MIDP_Streamlit.git](https://ljedd2-midp-streamlit-intro-kizzcq.streamlitapp.com/)  

---
## 9️⃣ Team Structure 

| 이름 | 역할 |
| ----- | ---- |
| 🐯 이정은 | 팀장 & 서기 (일정 기록, 회의록 정리) , 자료 정리 및 총 취합 , 응원, 가설 1 데이터 수집 및 분석 (EDA)  담당 , Streamlit page 초안 구상 |
| 🦁 구자현 | 아이디어뱅크 , 가설 2 데이터 수집 및 분석(EDA) 담당, 깃허브 Pull Request 관리 , Streamlit 베이스라인 코드 구축   |
| 🦁 문종현 | 팀원 깃 허브 교육 담당 가설 3 데이터 수집 및 분석(EDA) 담당, 결과보고서 작성 및 최종 파일 검토, Streamlit 베이스라인 코드 구축  |
| 🦁 안혜윤 |  PPT 작성 및 결과 보고회 발표자 , 결과보고서 작성 및 검토 응원단장, 가설 4 데이터 수집 및 분석(EDA) 담당  |
| 🦁 문영운 &nbsp;| 데이터 수집을 위한 훌륭한 영업사원 , PPT 작성 및 결과 보고회 발표자, 가설 5 데이터 수집 및 분석(EDA) 담당  |

---

## ❓핵심 INSIGHT
<img src="https://github.com/LJEDD2/MIDP_Streamlit/blob/main/Result/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C15.png">
<img src="https://github.com/LJEDD2/MIDP_Streamlit/blob/main/Result/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C8.png">
<img src="https://github.com/LJEDD2/MIDP_Streamlit/blob/main/Result/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C11.png">
<img src="https://github.com/LJEDD2/MIDP_Streamlit/blob/main/Result/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C12.png">


## 📑 프로젝트 배경
#### 1. 초등학교 시험 폐지
- 2011년 서울을 시작으로 전면 폐지가 되었지만, 수많은 찬반 논란이 존재하고 있다.

#### 2. 학업 성취도의 하락세
- 학업성취도의 지속적인 하락세와 양극화 현상
- **PISA** 
    - 학업성취도 국제비교연구로 OECD 각국 교육정책 수립의 기초자료를 제공하기 위해 만 15세 학생을 대상으로 읽기(글 이해력), 수학, 과학 능력을 평가하는 프로그램
    - 국제 학업 성취도에서 Reading, Math, Science 과목에서 순위가 떨어지고 있는 상황

#### 3. 사교육의 확대
- 사교육 참여 인원은 점점 늘어나고 있지만 학업 성취도는 떨어지고 있는 문제상황에 대한 분석과 해결 방안을 제시

---

## 📝 Hypothesis 
🗓️ 시험 폐지 , 자유학기제 시행 이후에도 매년 사교육비 지출은 꾸준히 증가하는 추세이다.   
- 본 프로젝트를 통해 시험이 폐지된 이후 10년 간 대한민국의 교육 정책에 어떤 변화가 생겼는지,   
그리고 현재 시험 부활에 대한 논의가 다시 이루어지게 된 배경에 대해 조금 더 자세히 알아보고자 한다.   

1. 초-중학생 사교육 참여율이 점점 증가하고 있다.  
2. 수능과 관련된 교과목을 중점으로 사교육을 병행할 것이다.
3. 학원 및 보습 교육 물가지수에는 큰 영향을 미쳤을 것이다.  
4. 사교육은 ‘사설학원’에서 가장 많이 이루어지고 있을 것이다.
5. 청소년들이 점점 학업에 흥미를 잃어가고 있으며, 학업 성취도 또한 하락세일 것이다.
6. 코로나 이후 학업을 중단하는 청소년들이 늘어났을 것이다. 

---

## 📥 Dataset

- 🔗 [지역별 1인당 월평균 사교육비 지출 현황 (2011 ~ 2022)](https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1PE202&vw_cd=MT_ZTITLE&list_id=H1_10_005&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE)  
- 🔗 [각 학교급 과목별 1인당 월 평균 사교육비 지출 현황  ](https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1PE202&vw_cd=MT_ZTITLE&list_id=H1_10_005&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE)  
- 🔗 [서울시 사설학원 통계(연도/ 구별/ 사설학원 (학교교과교습학원))](https://data.seoul.go.kr/dataList/195/S/2/datasetView.do)  
- 🔗 [학업성취도 평가(교과별 성취수준 비율)](https://www.index.go.kr/potal/main/EachDtlPageDetail.do?idx_cd=1539) 
- 🔗 [국제학업성취도평가(PISA)](https://www.index.go.kr/potal/main/EachDtlPageDetail.do?idx_cd=1539) 
- 🔗 [중고등학생 학업성취 지표집](https://naea.kice.re.kr/prtl/rept/info/rate-year) 
- 🔗 [서울시 학생의 학교생활 만족도 통계](https://data.seoul.go.kr/dataList/10779/S/2/datasetView.do) 
- 🔗 [원격수업 여부․효과성 여부 및 비효율적인 이유 (주된응답, 18세 이하 인구)](https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1SSCV061R&vw_cd=MT_ZTITLE&list_id=B_7_D220&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE) 
- 🔗 [서울시 학업성취수준 비율 통계](https://data.seoul.go.kr/dataList/10768/C/2/datasetView.do) 
- 🔗 [2011~20년 서울시 자치구별 초중고 학업중단률 ](https://data.seoul.go.kr/dataList/10713/C/2/datasetView.do) 
- 🔗 [서울시 유학생 현황 통계(12~20년)](https://data.seoul.go.kr/dataList/10802/C/2/datasetView.do;jsessionid=B2362306095F4A8304B584194340C61E.new_portal-svr-21) 
- 🔗 [etc](https://www.notion.so/MiD-9f2b50c7238a4edca1fc07a2dc95f7a9#903d1302da864db590d37bc9c3b73a8a)
---
### 💡개선할점

```
| 전체적인 페이지 로딩 속도 개선 
    |- folium 렌더링 속도 개선
    |- 캐싱 코드 추가
    |- 시각화 아래에 설명 및 인사이트 추가
```


