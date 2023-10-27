import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# GUI 애플리케이션을 생성
root = tk.Tk()
root.title("감정 그래프")

# 날짜와 감정을 저장할 리스8
dates = []
emotions = []


# '추가' 버튼을 누를 때 호출될 함수
def add_entry():
    date = date_entry.get()
    emotion = emotion_entry.get()

    if date and emotion:
        dates.append(date)
        emotions.append(emotion)
        date_entry.delete(0, tk.END)
        emotion_entry.delete(0, tk.END)
    else:
        messagebox.showerror("오류", "날짜와 감정을 모두 입력하세요.")


# '그래프 그리기' 버튼을 누를 때 호출될 함수
def draw_graph():
    if len(dates) == 0:
        messagebox.showerror("오류", "데이터가 없습니다.")
    else:
        fig, ax = plt.subplots()
        ax.plot(dates, emotions, marker='o', linestyle='-')
        ax.set_xlabel('날짜')
        ax.set_ylabel('감정')
        ax.set_title('감정 그래프')

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()


# 레이블과 입력 필드
date_label = ttk.Label(root, text="날짜:")
date_entry = ttk.Entry(root)
emotion_label = ttk.Label(root, text="감정:")
emotion_entry = ttk.Entry(root)

# '추가' 버튼
add_button = ttk.Button(root, text="추가", command=add_entry)

# '그래프 그리기' 버튼
graph_button = ttk.Button(root, text="그래프 그리기", command=draw_graph)

# 위젯 배치
date_label.pack()
date_entry.pack()
emotion_label.pack()
emotion_entry.pack()
add_button.pack()
graph_button.pack()

root.mainloop()
