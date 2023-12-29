# n개 간격의 원소들
# num_list와 n이 주어질때 배열읠 처음부터 마지막까지 n개의 간격으로 출력

def solution(num_list, n):
    return num_list[::n]

print(solution([4,2,6,1,7,6],2))