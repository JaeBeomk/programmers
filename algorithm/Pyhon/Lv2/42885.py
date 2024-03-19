# 구명보트 LV2 Greedy알고리즘
# 무인도에 갇힌 사람을 구명보트로 구출 - > 2명씩 무게제한도 있음
# 무게제한을 고려해 최소의 보트 구하기

def solution(people, limit):
    answer = 0
    people.sort()

    start = 0
    end = len(people) - 1
    
    # 2명씩 밖에 타지 못하기 때문에 맨 앞과 맨 뒤만 비교해서 탈 수 있는지 확인
    while end - start > 0 :
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
        else:
            end -= 1
        answer += 1
        
    # 무게는 초과하지 않지만 한 명만 남는 경우
    if end == start:
        answer += 1
    return answer


print(solution([70, 50, 80, 50],100)) #3
print(solution([70, 80, 50],100)) #3