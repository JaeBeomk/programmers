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
from baseNum import base_num,score,playBall



# window 생성
main=tk.Tk()
main.title("숫자야구")

# 수식 입력용 창
expression=tk.Label(main,text='입력',height=3,width=20,font=('',20),bg='grey')
expression.grid(row=0,column=0,columnspan=4,sticky="nsew")

# 정답 입력용 창

# 정답 입력 후 버튼 

# 정답 확인 창
result_label=tk.Label(main,text="?정답?",height=2,width=20,font=('',20),bg="grey")
result_label.grid(row=1,column=0,columnspan=4,sticky="nsew")

# 작동
main.mainloop()
