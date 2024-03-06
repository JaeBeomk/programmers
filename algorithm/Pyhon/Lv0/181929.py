# 원소들의 곱과 합
# 정수리스트가 주어질 때, 모든원소들의 곱이 모든원소들의 합의 제곱보다 작으면 1 크면 0
# 곱을 구하려면?

def solution(num_list):
    answer = 0
    a=1 # 곱 시작
    b=sum(num_list) # 모든 원소들의 합
    b= b**2 # 합의 제곱
    for i in num_list:
        a*=i
    print(a,b)
    
    return 1 if a<b else 0

print(solution([3,4,5,2,1])) #1