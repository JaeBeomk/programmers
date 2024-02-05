# JadenCase 문자열 만들기
# 모든단어 첫글자가 대문자로
# 문자열을 공백으로 나누고 원소를 슬라이싱해서 upper랑 lower로 변환?

def solution(s):
    answer = ''
    ans=[]
    sp=s.split(' ')
    # print(s,len(s))
    for i in range(len(sp)):
        answer+=sp[i][0].upper() # 앞글자 대문자
        answer+=sp[i][1:].lower() # 전체 소문자
        ans.append(answer)
        answer=''
    # print(s)
    answer=' '.join(ans) # join으로 합치기
    return answer

# 열심히 풀었지만... 답은 간단했다,... python ㅁㅊㄴ
# title() : 문장의 모든 단어의 첫 글자를 대문자로, 나머지는 소문자
# capitalize(): 문장의 첫 글자만 대문자로, 나머지는 소문자

def solution1(s):
    answer = ''
    s=s.split(' ')
    for i in range(len(s)):
        # capitalize 내장함수를 사용하면 첫 문자가 알파벳일 경우 대문자로 만들고
        # 두번째 문자부터는 자동으로 소문자로 만든다
        # 첫 문자가 알파벳이 아니면 그대로 리턴한다
        s[i]=s[i].capitalize()
    answer=' '.join(s)
    return answer
    

def solution2(s):
	return s.title()


print(solution("3people unFollowed me"))
print(solution("for the last week"))