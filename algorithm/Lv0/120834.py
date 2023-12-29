# 외계행성의 나이
# 이상한 행성에 갔는데 나이가 알파벳이다
# a=0 b=1 c=2 23=cd 51=fb 
# age가 주어질때 알파벳 나이를 리턴
# 아스키코드ascii -> 문자 chr()
# 문자열 -> 아스키코드로 ord()
# age => 문자열로 변경 후 for 문으로 한자씩 나눠 chr

def solution(age):
    answer = ''
    for i in str(age):
        #print(chr(age))
        #print(i)
        #print(chr(int(i)+97))
        answer += chr(int(i) + 97)
    return answer

print(ord("a")) # 0 + 97
print(ord("j"))
print(solution(23)) #cd




