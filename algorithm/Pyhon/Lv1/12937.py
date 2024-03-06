# 정수 num이 짝수일 경우 Even을 반환 홀수일 경우 Odd 를 반환
def solution(num):
    answer = ''
    if num % 2==0:
        answer="Even"
    else:
        answer="Odd"
    return answer

print(solution(3))