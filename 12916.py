# 문자열 내 p와y의 개수
# 대소문자가 섞인 s 가 주어지는데 p / y의 개수를 비교해 같으면 true 다르면 false 리턴
# 대소문자 구분을 안하는 문제여서,,, lower 추가
def solution(s):
    answer = True
    p=0
    y=0
    s=s.lower()
    for i in s:
        # print(i) 
        if i=='p':
            p+=1
        elif i=='y':
            y+=1
    print(p,y)
    if p !=y:
        answer=False
    return answer

print(solution("pPoooyY"))
print(solution("Pyy"))