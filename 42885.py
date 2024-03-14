# 구명보트 LV2 Greedy알고리즘
# 무인도에 갇힌 사람을 구명보트로 구출 - > 2명씩 무게제한도 있음
# 무게제한을 고려해 최소의 보트 구하기
# stack 구조로 구하자
# 최소로 구해야 하므로 두개를 지우자
# 틀려서 다시
def solution(people, limit):
    people=sorted(people)
    cnt=0
    boat=0
    weigth=[]
    weigth_r=[]
    for i in people:
        # print(i)
        weigth.append(i)
        boat+=1
        # print(weigth)
        if boat==2 and sum(weigth)<=100:
            # print(boat,"bbbbbbbbbbb")
            cnt+=1
            boat=0
            weigth=[]
        if sum(weigth)>limit:
            weigth_r.append(weigth.pop())
            # print(weigth_r,"rrrrrrrrr")
    if len(weigth_r)>0 or len(weigth)>0:
        # print(len(weigth_r))
        # print(len(weigth))
        cnt+=len(weigth_r)+len(weigth)
        
    return cnt
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