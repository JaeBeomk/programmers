# 암호해독
# 머쓱이는 적군 암호체계를 깨달았다
# 암호 문자열중 배수만 뽑아냄

def solution(cipher, code):
    answer = ''
    for i in range(code-1,len(cipher),code):
        # print(cipher[i])
        answer+=cipher[i]
    return answer

print(solution("dfjardstddetckdaccccdegk",4)) # attack