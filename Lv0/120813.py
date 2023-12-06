# 짝수는 싫어요
def solution(n):
    answer = []
    for i in n:
        if i % 2 !=0:
            answer.append(i)
            return answer

a=10
b=15
answer = []
for i in range(a+1):   
    if i % 2 !=0:        
        answer.append(i)
print(answer)