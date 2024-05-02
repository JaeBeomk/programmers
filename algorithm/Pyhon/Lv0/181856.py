# 배열비교하기
# 배열의 길이 비교하고 길이가 같다면 모든 원소합이 큰쪽이 크고 같다면 같다
# 두 정수 배열 arr1과 arr2가 주어질 때, 위에서 정의한 배열의 대소관계에 대하여 arr2가 크다면 -1, arr1이 크다면 1, 두 배열이 같다면 0을 return 하는 solution 함수를 작성해 주세요.

def solution(arr1, arr2):
    if len(arr1) == len(arr2):
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr1) == sum(arr2):
            return 0
        else: return -1
    else:
        if len(arr1) > len(arr2):
            return 1
        else: return -1

print(solution([49, 13],[70, 11, 2]))  # -1
