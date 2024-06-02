# 이상한 문자열 만들기
# 단어가 띄어져있는데 띄어쓰기 기준으로 홀수번은 대문자 짝수번은 소문자
# count를 하나 지정해서 순번을 정해주면 편할것같다...


def solution(s):
    answer = ''
    count=0
    for i in range(len(s)):
        if s[i]==' ':
            count=0
        else:
            count+=1
            
        if count%2==0:
            answer+=s[i].lower()
        elif count%2==1:
            answer+=s[i].upper()
    return answer


print(solution("try hello world")) #"TrY HeLlO WoRlD"