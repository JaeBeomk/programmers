# 양꼬치
# 10인분 먹으면 음료수 한개 서비스
# 1인분 12000 음료 2000원
# 양꼬치 n 인분 음료 k 개 먹으면 얼마임?
def solution(n, k):
    k = k- (n // 10)
    return (12000*n) + (2000*k)
print(solution(10,3))