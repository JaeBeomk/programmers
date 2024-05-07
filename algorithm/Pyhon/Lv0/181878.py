# 원하는 문자열 찾기
# 문자열이 존재하면 1 아니면 0 return
# 대소문자 구분 안함


def solution(myString, pat):
    myString=myString.upper()
    pat=pat.upper()
    if myString.find(pat) !=-1:
        return 1
    else: return 0

print(solution("AbCdEfG","aBc"))
