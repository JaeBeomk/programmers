# 숫자야구
# 3개의 숫자를 랜덤하게 만든다. 
# 자리와 값이 일치하면 strike
# 값이 존재하면 ball
# 숫자는 중복하지 않고 자리와 숫자를 모두 맞추면 strike out

# random 모듈에서 randint만 사용
from random import randint
# GUI로 구축
import tkinter as tk

# 숫자야구 정답 3자리
def base_num():
    num=[] # ball count 담을 배열
    i=0
    new_num=0
    while i<3:
        new_num=randint(0,9)
        if new_num not in num:
            num.append(new_num)
            i+=1
    return num

# 정답 확인
print(base_num())

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
