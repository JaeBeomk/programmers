#  뒤에서 5등까지
# 정수 배열이 주어지는데 가장 작은 수 5개를 오름차순으로 담은 리스트 출력
# num_list를 정렬 후 뒤집고 pop해서 append하자
# 다른 분 정답을 봤는데 그냥 sorted(num_list)[:5] 로 정렬하고 바로 뒤부터 출력하면되네
# Good
def solution(num_list):
    answer = []
    num_list.sort()
    num_list.reverse()
    for i in range(5):
        answer.append(num_list.pop())
        
    return answer

print(solution([12, 4, 15, 46, 38, 1, 14]))