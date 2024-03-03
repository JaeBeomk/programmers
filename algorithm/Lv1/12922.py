# 수박수박수박수박수박수?
# 길이가 n 인데 수박수박 반복

def solution(n):
    answer = ''
    for i in range(n):
        # print(i)
        if i %2==0:
            answer+='수'
        elif i%2==1:
            answer+='박'
    return answer

print(solution(3)) # 수박수
# print(solution(4)) # 수박수박
