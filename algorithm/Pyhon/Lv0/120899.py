# 가장 큰 수 찾기
# 큰 수와 그 수의 인덱스를 담은 배열 추출

def solution(array):
    # print(max(array))
    # print(array.index(max(array)))
    return [max(array),array.index(max(array))]

print(solution([1, 8, 3]))
