# 중앙값구하기
# python은 버블정렬 없이 sorted 함수 사용하자...
def solution(array):
    array=sorted(array)
    i=len(array)//2
    return array[i]

array=[9, -1, 0]
array=sorted(array)
le=len(array)//2
print(le)
print(array)
print(array[le])