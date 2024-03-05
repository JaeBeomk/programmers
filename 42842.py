# 카펫
# 전체 카펫의 크기 구하기
# 갈색은 겉 노랑은 안
#yellow = x * y
#brown = 2*(x+y) + 4
#(brown - 4)//2 = x + y

# def solution(brown, yellow):
#     answer = []
#     total=brown+yellow
#     for i in range(1,total):
#         # print(i)
#         if total % i == 0 :
#             answer.append(i)
#     answer.reverse()
#     # print(answer)
#     # print(len(answer)//2)
#     for i in range(len(answer)//2+1):
#         a=answer.pop()
    
#     print(a)
#     if a*a==total:
#         return [a,a]
#     else:
#         return [answer.pop(),a]
    
def solution(brown, yellow):
    x = 0
    sum = (brown - 4) // 2

    for r in range(sum):
        if r * (sum-r) == yellow:
            x = max(r, sum-r)
            break
            
    answer = [x + 2 , sum-x + 2]
    return answer

print(solution(10,2)) #[4,3]
print(solution(8,1)) # [3,3]
print(solution(24,24)) #[8,6]