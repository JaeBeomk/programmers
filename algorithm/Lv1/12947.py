# 하샤드 수
# 양의 정수 x 가 하샤드 수이려면 x의 자릿수의 합으로 x 가 나누어져야 한다
# 맞으면 true 아니면 false
# 일단 자릿수의 합을 구해보자

def solution(x):
    # 자릿수 합
    x_list=list(str(x))
    y=0
    for i in x_list:
        y+=int(i)
    print(y,type(y))
    # 하샤드 수인지
    return x % y ==0


print(solution(10)) # T
print(solution(12)) # T
print(solution(11)) # F
print(solution(13)) # F