# 점프와 순간이동
# 거리 N이 주어지고 점프는 1칸을 가면 1의 건전지가 달고
# 순간이동은 (현재까지 이동 거리) X 2의 거리를 이동 가능
# 최소의 건전지 사용한 답 구하기 = 탐욕법(Greedy) 풀이
# 위치 x 에서 0으로 갈떄 2의 배수라면 순간이동 홀수라면 배터리 카운트


def solution(n):
    answer = 0 
    while n > 0 :
        if n % 2 == 1 :
            answer += 1
        n //= 2
    return answer

print(solution(5000)) #5
# print(solution(6)) #2
