import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Streamlit 앱 제목 설정
st.title("꺾은선 그래프 예제")

# 사용자에게 데이터 입력 받기
data = st.text_area("데이터 입력 (쉼표로 구분)", "1,2,3,4,5")

# 데이터 파싱
data = data.split(',')
data = [int(x) for x in data]

# 꺾은선 그래프 그리기
fig, ax = plt.subplots()
ax.plot(data)

# 그래프 제목 및 레이블 설정
ax.set_title('꺾은선 그래프')
ax.set_xlabel('X 축')
ax.set_ylabel('Y 축')

# Streamlit에 그래프 표시
st.pyplot(fig)
