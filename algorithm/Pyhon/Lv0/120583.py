# 중복된 숫자 개수
# 정수배열 안에 n 이 몇개 들었는지

def solution(array, n):
    answer = 0
    for i in array:
        if n== i:
            answer+=1
    return answer

# print(solution([1, 1, 2, 3, 4, 5],1))
print(solution([0, 2, 3, 4]	,1))