#연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다.
# 양의 정수 a와 b가 주어졌을 때, a ⊕ b와 b ⊕ a 중 더 큰 값을 return 하는 solution 함수를 완성해 주세요.
def solution(a, b):
    answer = 0
    str_sum=str(a)+str(b)
    str_sum1=str(b)+str(a)
    
    if int(str_sum)>=int(str_sum1):
        answer=str_sum
    else:
        answer=str_sum1
    return int(answer)
print(solution(10,1))


