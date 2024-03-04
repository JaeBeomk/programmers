# 짝지어 제거하기
# 알파벳 소문자로 이루어진 문자열 2개가 붙어있는짝을 찾고 제거
# 모든 문자열 짝이 제거되면 종료
# 성공적 수행 =1 실패 =0
# 스택을 이용해 해결 

def solution(s) :
    stack = []

    for value in s :
        if not stack :
            stack.append(value)
        else :
            if stack[-1] == value :
                stack.pop()
            else :
                stack.append(value)

    if stack :
        return 0

    return 1
print(solution("baabaa")) # 1
# b aa baa -> bbaa -> aa -> ""
# print(solution("cdcd")) # 0