# 두 정수 사이의 합
# 두 정수 a,b가 주어졌을때 a-b 사이에 속한 모든 정수의 합을 리턴
# 반복문 시점만 생각하면되나?
# sum(range()) 함수를 처음보는데 이거 좋네

def solution(a, b):
    
    # answer = 0
    # if a > b:
    #     for i in range(b,a+1):
    #         answer+=i
    # elif b> a:
    #     for i in range(a,b+1):
    #         answer+=i
    # elif a==b:
    #     answer=a
    # return answer
    # 다르게 풀면 a>b 크면 두개를 바꿔주고 범위만큼 더한다? 개사기 ㅇㅈ
    if a> b:
        a,b=b,a
    return sum(range(a,b+1))

print(solution(3,5)) #12
print(solution(5,3)) #12
print(solution(3,3)) #3