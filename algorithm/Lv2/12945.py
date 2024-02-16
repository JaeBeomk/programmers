# 피보나치 수
#  F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수
# F(2) = F(0) + F(1) = 0 + 1 = 1
# F(3) = F(1) + F(2) = 1 + 1 = 2
# F(4) = F(2) + F(3) = 1 + 2 = 3
# F(5) = F(3) + F(4) = 2 + 3 = 5
# 2이상 n이 입력될때 1234567 로 나눈 나머지를 리턴

def solution(n):
    answer = 0
    F=0
    x=0
    y=1
    # 피보나치수는 수를 두개의 변수에 담아서 구해보자
    for i in range(2,n+1):
        # print(i)
        # 3이였을때는 한번 더 사용해줘야한다.
        if i==3:
            y=1
        F=x+y
        # print(x,y,F,"FFFFFFFFFFFFFF")
        x=y
        y=F
    if n >=2 :
        F=F%1234567
    return F

print(solution(3)) # 2
print(solution(5)) # 5
