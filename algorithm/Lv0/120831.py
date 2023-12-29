# 짝수의 합
# n 이 주어질때 n 이하 짝수를 모두 더한 값
# n 까지 반복하기 위해서는 +1 을 해주어야 한다.
def solution(n):
    answer = 0
    for i in range(n+1):
        if i %2==0:
            answer+=i
    return answer
print(solution(10))
print(solution(4))