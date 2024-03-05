# 연속 부분 수열 합의 개수
# 원형 수열로 만들수 있는 합의 개수
# set 함수로 배열속 element 중복제거
def solution(elements):
    sum_set = set()
    length = len(elements) # 5
    # 1~5 0~4 까지 반복
    for i in range(1, length+1) :
        for j in range(length) :
            if j + i > length :
                sum_set.add(sum(elements[j:]) + sum(elements[:j+i-length]))
            else :
                sum_set.add(sum(elements[j:j+i]))
    return len(sum_set)

print(solution([7,9,1,1,4])) # 18 