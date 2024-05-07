# n보다 커질 때까지 더하기
# numbers의 원소를 앞에서부터 하나씩 더하다가 그 합이 n보다 커지는 순간 이때까지 더했던 원소들의 합을 return 

def solution(numbers, n):
    answer = 0
    for i in numbers:
        answer+=i
        if answer>n: return answer
    



print(solution([34, 5, 71, 29, 100, 34],123))
