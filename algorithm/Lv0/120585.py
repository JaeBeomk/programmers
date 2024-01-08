# 머쓱이보다 키큰사람
# 배열과 키가 주어질때 키큰사람 수

def solution(array, height):
    answer = 0
    for i in array:
        if i>height:
            answer+=1
    return answer

print(solution([149, 180, 192, 170],167))