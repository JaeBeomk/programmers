# 제곱수 판별하기
# 어떤 자연수를 제곱했을때 나오는정수 = 제곱수 
# n 이 주어질때 제곱수면 1 아니면 2
# n 이 제곱수인지를 판단하려면 ???
# 제곱수... 4 9 16....등등
# 반복문 후 i의 제곱값이 n과 같은지

def solution(n):
    for i in range(n):
        if i**2==n:
            # print(i)
            return 1
    return 2
    
print(solution(144))
print(solution(4))
print(solution(6))