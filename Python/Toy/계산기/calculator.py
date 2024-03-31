# 계산기 GUI
# 설계 = 메인필드,입력필드,결과,버튼
# 계산기 기능은 cal.py참고
# tkinter 라이브러리 사용해 GUI설계
import tkinter as tk

# 계산기능 python으로 동작하다보니 제곱은 ** 등으로 처리가능
def cal():
    # try except 구문으로 처리 중 에러 제거
    try:
        result=eval(expression.get("1.0",tk.END))
        result_label.config(text=str(result))
    # Error처리
    except Exception as e:
        result_label.config(text="Error")

# 처리 완료 후 처음상태로
def clear():
    expression.delete("1.0",tk.END)
    result_label.config(text="")

# 버튼 구현 (내 노트북에 맞게)
buttons =[
    '7','8','9','+',
    '4','5','6','-',
    '1','2','3','*',
    'C','0','=','/'
]

# window 만들고 타이틀
main=tk.Tk()
main.title("계산기")

# 수식입력용 text
expression=tk.Text(main,height=3,width=20,font=('',20),)
expression.grid(row=0,column=0,columnspan=4,sticky="nsew")

# 결과값 표시
result_label=tk.Label(main,text="?정답?",height=2,width=20,font=('',20),bg="yellow")
result_label.grid(row=1,column=0,columnspan=4,sticky="nsew")

# click시 돌아가게
def click(value):
    # = 누를시 계산
    if value=="=":
        cal()
    # 원복
    elif value=="C":
        clear()
    # 그 외는 계산식 생성
    else:
        expression.insert(tk.END,value)

# 모양이쁘게 행열 설정
row=2
col=0

# buttons 반복해서 UI로 만들기
for button in buttons:
    btn=tk.Button(main,
                  text=button,
                  # lambda를 이용해 button클릭시 한번에 계산
                  command=lambda b=button: click(b),
                  width=10,height=8)
    btn.grid(row=row,column=col,sticky="nsew")

    main.grid_rowconfigure(row,weight=1)
    main.grid_columnconfigure(col,weight=1)
    
    # 행row/열col 증가
    col+=1
    if col>3:
        col=0
        row+=1
# window 작동 x누를때 까지 안꺼짐
main.mainloop()
    