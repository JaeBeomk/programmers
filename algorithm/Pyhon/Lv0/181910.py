# https://school.programmers.co.kr/learn/courses/30/lessons/181910?language=python3
# mystring , n 이 주어질때 n 의 글자로 이루어진 문자열 리턴

def solution(my_string, n):
    return my_string[-n:]


print(solution("ProgrammerS123",11))
