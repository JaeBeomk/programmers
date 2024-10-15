# https://school.programmers.co.kr/learn/courses/30/lessons/181926
# 수 조작


def solution(n, control):
    for i in control:
        if i=='w': n+=1
        elif i=='s': n-=1
        elif i=='d': n+=10
        elif i=='a': n-=10
    return n
    # key=dict(zip(['w','s','d','a'],[1,-1,10,-10]))
    # return n+sum([key[c] for c in control])


print(solution(0,"wsdawsdassw"))
