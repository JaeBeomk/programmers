# 약수의합
# 정수 n을 받아 n의 약수를 모두 더한값을 리턴하는 함수
# 
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n % i==0:
            answer+=i
            # print(i)
    return answer

print(solution(12)) # 28 