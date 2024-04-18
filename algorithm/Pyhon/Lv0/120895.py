# 인덱스 바꾸기
# 문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때, 
# my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return 
# list문은 문자열index 위치에서 쉽게 변경 가능

def solution(my_string, num1, num2):
    my_string=list(my_string)
    my_string[num1],my_string[num2]=my_string[num2],my_string[num1]
    my_string=''.join(my_string)
    return my_string

print(solution("hello",1,2)) # hlelo
