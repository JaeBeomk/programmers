# 배열 원소의 길이
# strlist가 매개변수로 주어진다.
# 배열속 문자열의 크기를 배열로 return
# 난이도가 생각보다 쉬우니.. 더 간편하게 짜볼까?
# list와 map으로 묶으면 라인으로 끝낸다

def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer

def sol(strlist):
    return list(map(len,strlist))


print(sol(["We", "are", "the", "world!"]))