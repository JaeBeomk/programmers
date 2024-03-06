# 없는 숫자 더하기
# 0-9 까지 숫자중 일부가 들어있는 정수 배열에서 찾을수 없는 0-9까지를 모두 더한 수를리턴
# 다른이 풀이 보는데 45-sum(numbers) 좋은데...?
def solution(numbers):
    answer = 0
    for i in range(0,10):
        if i in numbers:
            pass
        else:
            answer+=i
    return answer


print(solution([1,2,3,4,6,7,8,0])) # 14 =9,5