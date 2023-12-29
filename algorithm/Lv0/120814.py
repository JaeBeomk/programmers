# 피자나눠먹기(1)
# 7조각으로 나눠줌
# n 명이 1조각 이상 먹으려면?
# n/7 을 했을때 소수점을 올림해야함
# 인상깊은 답 ...return (n-1) //7 +1
def solution(n):
    answer = n/7
    min = n//7
    if answer > min:
        answer = int(answer)+1
    else:
        answer = int(answer)
    
    
    return answer
def sol(n):
    return (n-1)//7+1
print(sol(8))