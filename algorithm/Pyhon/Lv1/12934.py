# 정수 제곱근 판별
# 임의 양의정수 n에 대해 n이 x의 제곱인지 판단하려함
# n이 x의 제곱이면 x+1 제곱 리턴 n이 양의 정수 x 의 제곱이 아니면 -1 리턴


def solution(n):
    answer = 0
    for i in range(0,n+1): # 0~n 값을 반복
        if i**2 == n:
            answer= (i+1)**2
            break
        else:
            answer= -1
    return answer

print(solution(121)) #144
print(solution(3)) #-1