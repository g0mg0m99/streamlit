import tkinter as tk
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


#리스트를 사용하여 감정 이력을 저장합니다.
emotion_records = []

#tkinter 창 생성
root = tk.Tk()
root.title("(가제)모바일 정신건강 도우미")

#라벨 생성
label_emotion = tk.Label(root, text="오늘의 감정")
label_date = tk.Label(root, text="오늘의 날짜")
label_feedback = tk.Label(root, text="")

#사용자 입력을 받을 텍스트 상자 생성
entry_emotion = tk.Entry(root)
entry_date = tk.Entry(root)

#감정을 제출하는 함수
def submit():
    # 입력된 감정과 날짜를 가져옵니다.
    emotion = entry_emotion.get()
    date = entry_date.get()

    # 감정 데이터를 딕셔너리로 만들어서 리스트에 추가합니다.
    emotion_record = {"emotion": emotion, "date": date}
    emotion_records.append(emotion_record)  # 감정 이력 리스트에 추가

    # 감정 데이터를 출력합니다.
    feedback = f"감정: {emotion}, 날짜: {date}"
    label_feedback.config(text=feedback)  # 프로그램 창에 표시

#감정 이력을 표시하는 함수
def history():
    # 감정 이력을 출력합니다.
    feedback = "감정 이력:\n"
    for record in emotion_records:
        feedback += f"감정: {record['emotion']}, 날짜: {record['date']}\n"
    label_feedback.config(text=feedback)  # 프로그램 창에 표시

#감정을 제출하거나 이력을 표시하는 버튼을 생성하고 함수를 연결합니다.
button_submit = tk.Button(root, text="기록하기", command=submit)
button_history = tk.Button(root, text="기록 보기", command=history)

#그리드 레이아웃 사용
label_emotion.grid(row=0, column=0)
entry_emotion.grid(row=0, column=1)
label_date.grid(row=1, column=0)
entry_date.grid(row=1, column=1)
button_submit.grid(row=2, column=0)
button_history.grid(row=2, column=1)
label_feedback.grid(row=3, columnspan=2)  # 결과 메시지를 표시할 라벨

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


#tkinter 메인 루프 실행
root.mainloop()