# 나누어 떨어지는 숫자 배열
# arr의 각 요소중 divisor로 나누어떨어지는 값을 오름차순으로 정렬한 배열
# 배열을 배열로 돌려서 divisor로 나눴을때 나머지가 0이면 배열에 담고 정렬
# arr의 마지막 요소까지 갔는데 0으로 안나눠지면 ==> 배열이 비었다면 -1 리턴
def solution(arr, divisor):
    answer = []
    # print(arr[-1:])
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if answer==[]:
        answer.append(-1)    
            
    return sorted(answer)

print(solution([5, 9, 7, 10],5)) # [5,10]
print(solution([3,2,6],10)) # -1