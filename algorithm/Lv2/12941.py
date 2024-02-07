# 최솟값 만들기
# 길이가 같은 배열 a b 두개가 있다.
# 배열 a b 에서 한개의 숫자를 뽑아 두 수를 곱하고 이 과정을 배열길이만큼 반복
# 곱한값을 누적해 더한다. 이때 최종적으로 누적값이 최소가 되도록
# 1번의 경우 그냥 순차적으로 곱하면 해결이지만 
# 2번의 경우 문제다..
# 정렬을 이용해서 제일 작은수랑 제일 큰수를 곱하면 해결이지 않을까?

def solution(A,B):
    answer = 0
    la=len(A)
    A=sorted(A)
    B=sorted(B,reverse=True)
    # print(la)
    for i in range(la):
        answer+=A[i]*B[i]
    return answer

# print(solution([1, 4, 2],[5, 4, 4])) # 29
print(solution([1,2],[3,4])) #10