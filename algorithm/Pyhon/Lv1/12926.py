# 시저암호
# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 
# 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. 
# "z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수 return
# 아스키코드
# 문자열을 숫자로 ord()
# 숫자를 문자열로 chr()
# 알파벳은 총 26개
# 대소문자 구분으로 나누자

def solution(s, n):
    S=''
    print(ord("a"))
    # print(ord("z"))
    print(ord("A"))
    # print(ord("Z"))
    
    for i in s:
        if i.isupper():
            # 65 = A
            S+=chr((ord(i)+n-65)%26+65)

        elif i.islower():
            # 97 = a
            S+=chr((ord(i)+n-97)%26+97)
        elif i==' ':
            S+=' '
    return S


print(solution("xyz",3)) #abc
# print(solution("AB",1)) # BC
# print(solution("z",1)) # a
# print(solution("a B z",4)) # e F d
 