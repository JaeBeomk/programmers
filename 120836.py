# 순서쌍구하기
# 두개의 수의 곱이 n이 나오도록 하는수중 몇개가 나오나
# 최대로 나올수있는수는 n의 수
# 반복문으로 길이만큼 열심히!
# 시간초과넹...?
# 반복문을 두개에서 하나로 줄여야겠다...

def solution(n):
    answer = 0
    
    for i in range(n+1):
        for j in range(n+1):
            if i*j == n:
                # print(i,j,"i와j") 
                answer+=1
    return answer

print(solution(20))
print(solution(100))