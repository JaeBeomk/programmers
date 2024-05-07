# 길이에 따른연산
# 리스트 길이가 11이상이면 모든 원소 합
# 길이가 10이하면 모든원소의 곱
from functools import reduce
def solution(num_list):
    lnum=len(num_list)
    
    if lnum>=11: return sum(num_list)
    else: return reduce(lambda x,y :x*y,num_list)

print(solution([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]))
print(solution([2, 3, 4, 5]))
