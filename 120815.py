# 피자 나눠먹기(2)
# 6조각으로 주는데 모두 같은 수의 피자 조각을 먹어야 한다..
# 피자를 먹는사람 n
# 피자수 pizza
# 조각 수 s = pizza/6
# 최소 공배수 구하기... 
# 1 6 = 1
# 2 3 = 1
# 3 2 = 1
# 4 12 = 2
# 5 30 = 5


def solution(n):
    for i in range(n,n*6+1):
        if i%n==0 and i%6==0:
            return i/6

print(solution(5))