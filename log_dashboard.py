#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# CSV 불러오기
df = pd.read_csv("log_data.csv")

st.title("📊 AI 기반 로그 이상 탐지 대시보드")

# 테이블 출력
st.subheader("📄 전체 로그 데이터")
st.dataframe(df)

# 이상 탐지된 로그만 표시
st.subheader("🚨 이상 탐지 로그")
anomalies = df[df['Anomaly'] == 1]
st.dataframe(anomalies)

# 그래프: 이상 점수 분포
st.subheader("📈 이상 점수 분포 (Anomaly Score)")
fig, ax = plt.subplots()
ax.bar(df.index, df['Anomaly_Score'], color=["red" if a == 1 else "gray" for a in df['Anomaly']])
ax.set_xlabel("로그 순번")
ax.set_ylabel("Anomaly Score")
st.pyplot(fig)

# 생성형 AI 요약
st.subheader("🧠 생성형 AI 요약 (예시)")
st.markdown("""
> 사용자 `ahyeon`의 외부 이메일 전송 로그는 평균 이상 점수를 초과하였으며,  
> 데이터 유출 가능성이 높습니다. 긴급 대응을 권장합니다.
""")

