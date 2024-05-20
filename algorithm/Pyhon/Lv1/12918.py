# 문자열 다루기 기본
# 문자열s 의 길이가 4 or 6 이고 숫자로만 구성되어있는지


def solution(s):
    ls=len(s)
    # print(ls)
    if s.isdigit():
        if ls==4 or ls==6:
            return True
        else: return False
    else: return False
    
    # 이게 제일 좋은 표현이네...
    return s.isdigit() and ls in [4,6]

# print(solution("a234"))
print(solution("12345"))

