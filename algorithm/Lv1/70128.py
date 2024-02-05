# 내적
# 길이가 같은 두 1차원 정수 배열 a b 내적을 return
# 이때 내적의 길이는 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 
# n 은 a b 의 길이

def solution(a, b):
    answer = 0
    for i in range(len(a)):
        # print(i)
        answer+= a[i]*b[i]
    return answer


print(solution([1,2,3,4],[-3,-1,0,2])) # 3
print(solution([-1,0,1],[1,0,-1])) # -2