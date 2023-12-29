# 배열 두배 만들기
#  인상깊은 다른이 답 return [num*2 for num in numbers] 
def solution(numbers):
    answer = []
    l=0
    for i in numbers:
        answer.append(int(numbers[l])*2) 
        l=1+l
    return answer



