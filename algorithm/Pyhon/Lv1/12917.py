# 문자열 내림차순으로 배치하기
# 문자열 s에 나타나는 문자를 쿤것부터 작은순으로 정렬해 새로운 문자열 리턴
# 문자열을 ascii code로 변환해서 순서를 맞춘 후 다시 정렬
# ord() chr()
# 굳이 변환해서 안풀어도 괜찮네?

def solution(s):
    return ''.join(sorted(s,reverse=True))
    # answer = []
    # ans=''
    # for i in s:
    #     print(i)
    #     answer.append(ord(i))
    # answer.sort()
    # answer=reversed(answer)
    # for i in answer:
    #     ans+=(chr(i))
    # return ans

print(solution("Zbcdefg")) #"gfedcbZ"
