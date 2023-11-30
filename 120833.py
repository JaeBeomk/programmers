# 배열 자르기
# 배열과 정수 2개가 매개변수 배열의 n1 부터 n2 까지 자른 배열 리턴
# numbers 배열을 n1 부터 n2+1까지
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]
print(solution([1, 2, 3, 4, 5],1,3)) # [2,3,4]
print(solution([1, 3,5],1,2)) # [3,5]