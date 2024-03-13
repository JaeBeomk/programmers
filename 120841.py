# 점의 위치 구하기
# 사분면은 한 평면을 x축과 y축을 기준으로 나눈 네 부분
# 사분면은 아래와 같이 1부터 4까지 번호를매긴다
# x/y  = 1
# -x/y = 2
# -x/-y = 3
# x/-y =4

def solution(dot):
    if dot[0] < 0:
        if dot[1] >0:
            return 2
        else:
            return 3
    else:
        if dot[1] >0:
            return 1
        else:
            return 4

print(solution([2, 4]))