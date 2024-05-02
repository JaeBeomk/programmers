# 배열 회전시키기
# 배열과 방향이 주어질때 배열을 방향으로 이동

def solution(numbers, direction):
    if direction=="right": numbers=numbers[-1:]+numbers[-1]
    else: numbers=numbers[1:]+numbers[0]
    return numbers


# print(solution([1, 2, 3],"right")) # [3,1,2]
print(solution([4, 455, 6, 4, -1, 45, 6],"left"))
