import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Streamlit 앱 제목 설정
st.title("감정 및 날짜 데이터 시각화")

# 사용자로부터 데이터 입력 받기
emotion_data = st.text_area("감정 데이터 입력 (쉼표로 구분)", "1,2,3,4,5")
date_data = st.text_area("날짜 데이터 입력 (쉼표로 구분)", "2023-01-01,2023-01-02,2023-01-03,2023-01-04,2023-01-05")

# 데이터 파싱
emotions = emotion_data.split(',')
dates = date_data.split(',')

# 데이터 프레임 생성
df = pd.DataFrame({'날짜': dates, '감정': emotions})

# 날짜를 datetime 형식으로 변환
df['날짜'] = pd.to_datetime(df['날짜'])

# 그래프 그리기
fig, ax = plt.subplots()
ax.plot(df['날짜'], df['감정'])

# 그래프 제목 및 레이블 설정
ax.set_title('감정과 날짜의 관계')
ax.set_xlabel('날짜')
ax.set_ylabel('감정')

# X 축의 날짜 형식 설정
plt.xticks(rotation=45)

# Streamlit에 그래프 표시
st.pyplot(fig)
