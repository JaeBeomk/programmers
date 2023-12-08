# flag에 따랄 다른 값 반환하기
# a,b bool변수 flag 가 매개변수 
# flag 가 참이면 a + b 거짓이면 a-b
# if 문으로 풀면 되겠다

# 왜 틀리지? 아... True/False...?
def sol(a, b, flag):
    return (a+b) if flag==True else (a-b)

def solution(a, b, flag):
    if (flag == True):
        return (a+b)
    elif (flag ==False):
        return (a-b)


print(solution(-4,7,"true"))# a+b
print(solution(-4,7,"false"))# a-b