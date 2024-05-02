# n의 배수 고르기
# 배열에서 n의 배수가 아닌것 제거


def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n==0:
            answer.append(i)
    return answer

print(solution(3,[4, 5, 6, 7, 8, 9, 10, 11, 12]))
