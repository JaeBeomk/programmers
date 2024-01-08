# 이어붙인수
# 정수가 담긴 리스트 num_list가 주어질때 
# num_list의 홀수만 순서대로 이어 붙인 수
# 짝수만 순서대로 이어 붙인 수의 합을 return
# 문자열로 바꿔서 붙이고 다시 정수로 바꿔서 계산?

def solution(num_list):
    j=''
    h=''
    for i in num_list:
        if i %2 == 1:
            h+=str(i)
            
        elif i%2==0:
            j+=str(i)
    answer=int(h)+int(j)
    return answer
print(solution([3, 4, 5, 2, 1]	)) #393