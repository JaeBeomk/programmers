# 최댓값만들기 LV0
# 정수배열 numbers가 매개변수로 주어질때
# numbers의 원소 두개를 곱해 만들 수 있는 최댓값

def solution(numbers):
    numbers=sorted(numbers,reverse=True)
    return numbers[0]*numbers[1]


print(solution([1, 2, 3, 4, 5])) # 20