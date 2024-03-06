# 나머지가 1이되는 수 찾기
# 자연수 n이 주어질때 n을 x 로 나눈 
# 나머지가 1이되도록 하는 가장 작은 자연수 x return
# 

def solution(n):
    answer = []
    for x in range(1,n):
        if n%x==1:
            # print(x)
            answer.append(x)
    answer.reverse()
    return answer[-1]

print(solution(10)) # 3
print(solution(12)) # 11