# 가운데 글자 가져오기
# 단어 s의 가운데 글자를 반환 만약 단어 길이가 짝수면 2개 반환

def solution(s):
    answer = ''
    ls=len(s)
    a=ls//2 
    # 홀수일떄
    if ls%2: 
        answer+=s[a]   
    # 짝수
    else:
        answer+=s[a-1]+s[a]
    return answer


print(solution("abcde")) #c
print(solution("qwer")) # we
