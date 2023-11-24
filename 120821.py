# 배열 뒤집기
# reversed 함수를 사용 그런데... reversed는 내장함수여서 
# reversed(num_list)사용시 에러 출력
def solution(num_list):    
    return list(reversed(num_list))
print(solution([1, 2, 3, 4, 5]))