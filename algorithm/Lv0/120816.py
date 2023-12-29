# 피자 나눠먹기(3)
#  2 <= slice <= 10
# 나누는 조각 인원수가 주어질때 최소 한조각 먹으려면?
# ㅇreturn ((n-1)//slice) +1
def solution(slice, n):
    pizza= n/slice
    ceil=n//slice
    if pizza> ceil:
        pizza +=1
        
    return int(pizza)

print(solution(4,12))
print(solution(7,10))