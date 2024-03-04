# 카펫
# 전체 카펫의 크기 구하기
# 갈색은 겉 노랑은 안
# 틀려서 다시!


def solution(brown, yellow):
    answer = []
    total=brown+yellow
    for i in range(1,total):
        # print(i)
        if total % i == 0 :
            answer.append(i)
    answer.reverse()
    # print(answer)
    # print(len(answer)//2)
    for i in range(len(answer)//2+1):
        a=answer.pop()
    
    print(a)
    if a*a==total:
        return [a,a]
    else:
        return [answer.pop(),a]
print(solution(10,2)) #[4,3]
print(solution(8,1)) # [3,3]
print(solution(24,24)) #[8,6]