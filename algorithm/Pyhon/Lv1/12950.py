# 행렬의 덧셈
# 행과 열의 크기가 같은 두 행렬의 같은 행 같은 열의 값을 서로 더한 결과
# 행열을 만들어보자

def solution(arr1, arr2):
    for i in range(len(arr1)): # 배열 크기
        for j in range(len(arr1[0])): # 내부 배열의 크기
            arr1[i][j]+=arr2[i][j]
    
    # 0 01 10 11
    # 2차원 배열로 표현
    # for i in arr1:
    #     for j in i:
    #         print(j,end=" ")
    #     print()
    return arr1


print(solution([[1,2],[2,3]],[[3,4],[5,6]])) #[[4,6],[7,9]]
