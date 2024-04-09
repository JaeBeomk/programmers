# 숫자야구
# 3개의 숫자를 랜덤하게 만든다. 
# 자리와 값이 일치하면 strike
# 값이 존재하면 ball
# 숫자는 중복하지 않고 자리와 숫자를 모두 맞추면 strike out

# random 모듈에서 randint만 사용
from random import randint
# GUI로 구축
import tkinter as tk

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