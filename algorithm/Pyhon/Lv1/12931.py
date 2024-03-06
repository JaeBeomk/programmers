# 자릿수 더하기
# 자연수 N이 주어지면 N의 각 자릿수의 합을 구해 return
# 문자열로 바꿔서 한글자씩...빼서 더하자..

def solution(n):
    answer = 0
    for i in str(n):
        print(i)
        answer+=int(i)

    return answer

print(solution(123)) # 6