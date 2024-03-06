# 문자 반복 출력하기
# hello -> n 만큼 단어만큼 반복
# n=3 hhheeellllllooo 만큼 나오려면 배열list에 n 만큼 곱
def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer+=i*n
    return answer
print(solution("hello",3))