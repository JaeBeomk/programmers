# 숫자야구
# 3개의 숫자를 랜덤하게 만든다. 
# 자리와 값이 일치하면 strike
# 값이 존재하면 ball
# 숫자는 중복하지 않고 자리와 숫자를 모두 맞추면 strike out

# random 모듈에서 randint만 사용
from random import randint
# GUI로 구축
import tkinter as tk

# 이미 만든거 쓰자?
# from baseNum import base_num,score,playBall



# window 생성
main=tk.Tk()
main.title("숫자야구")

# 정답입력용 창
first=tk.Label(main,text="123",width=10,height=5,fg="red",relief="solid")
second=tk.Label(main,text="123",width=10,height=5,fg="blue",relief="solid")

# label 표시
first.pack()
second.pack()
# 작동
main.mainloop()
