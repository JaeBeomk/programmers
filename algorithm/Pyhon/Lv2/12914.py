# 멀리뛰기 LV2
# 멀리뛰기 연습중 한번에 1칸 또는 2칸 뛸수있다.
# 멀리뛰기의 칸수 n 일때 뛸수있는 방법 을 1234567 나눈 나머지
# 4칸이면 1,1,1,1 /1,2,1/1,1,2/2,1,1/2,2 총 5가지 방법 가능
# n=3 111 21 12 

def solution(num):
    if num==1:
        return 1
    elif num==2:
        return 2
    else:
        return solution(num-1)+solution(num-2)

# 피보나치 수열도 가능하네?        
def jumpCase(num):
    a, b = 1, 2
    for i in range(2,num):
        a, b = b, a+b
    return b




print(solution(4)) # 5
# print(solution(3)) # 3