# 제일 작은수 제거
# 가장작은 수를 제거한 배열을 리턴하고 배열이 비었으면 -1 리턴
# 역 정렬 하면 다시 변수에 담아야 한다. 
# 아 정렬이 아니라 그 자리 수를 없애야 하는구나? 
# 다음에 다시 짠다면 return [i for i in arr if > min(arr)] 으로 min 함수를 사용해보자
def solution(arr):
    i=sorted(arr,reverse=True)
    min=i.pop()
    if min in arr:
        arr.remove(min)
    # 빈 배열
    if arr==[]:
        arr= [-1]
    return arr

print(solution([4,3,2,1])) #[4,3,2]
print(solution([10])) #[-1]
print(solution([1,2,3,4]))  #[2,3,4]