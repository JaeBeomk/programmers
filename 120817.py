# 배열의 평균값
# numbers 매개변수로 배열이 주어지면 그거 평균값 구하기
# 배열의 길이를 구하고
# pop으로 하나씩 빼서 더해야 하나..?
# 배열의 index로 하나씩 뺄까 하였는데 
# python은 sum함수를 사용해 list배열의 값을 더할수있다.
def solution(numbers):
    i=sum(numbers)
    l=len(numbers)
    print(i)
    print(l)
    
    return float(i/l)

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]))