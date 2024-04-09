# 숨어있는 숫자의 덧셈(1)
# 매개변수안의 모든 자연수들의 합을 return
# 자연수는 한자리 수 -> 이러면 반복문으로 하나씩 뺴는 방법?
# 반복문으로 숫자인지 파악하는 isdigit() 사용해 검사
def solution(my_string):
    answer = 0
    # 반복문
    for i in my_string:
        if i.isdigit():
            answer+=int(i)
    return answer


print(solution("aAb1B2cC34oOp")) #10