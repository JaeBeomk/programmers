# 숫자야구 만들기
# 3개의 숫자를 랜덤하게 만든다. 
# 자리와 값이 일치하면 strike
# 값이 존재하면 ball
# 숫자는 중복하지 않고 자리와 숫자를 모두 맞추면 strike out

from random import randint

# 랜덤 숫자 만들기
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

# 스코어 확인
def score(ball,res):
    S_cnt=0 # strike
    B_cnt=0 # ball
    i=0 # 숫자
    while i<len(ball):
        if ball[i]==res[i]:
            S_cnt+=1
            i+=1
        elif ball[i] in res:
            B_cnt+=1
            i+=1
        else:
            i+=1
    return S_cnt,B_cnt

# 실제 플레이
def playBall():
    print("숫자 3개 입력하세요!")
    i=0 # 입력 숫자
    play=[]
    while i < 3:
        num=int(input("{}번째 숫자 입력:".format(i+1)))
        if num > 9:
            print("범위는 0~9 입니다.")
            continue
        if num in play:
            print("중복되는 숫자입니다.")
        else:
            play.append(num)
            i+=1
    return play

# 시작
QUE=base_num() # 정답

# 정답 확인
# print(QUE) 

challenge=0 # 도전 횟수

while 1: # python3에서는 while True 도 성능이 같음
    PLAY=playBall() # 플레이
    S_cnt,B_cnt=score(QUE,PLAY) 
    print("{} S {} B".format(S_cnt,B_cnt))

    # 정답시 멈춤
    if S_cnt==3:
        challenge+=1
        break
    else:
        challenge+=1

print("{}번 만에 맞추셨습니다.".format(challenge))
