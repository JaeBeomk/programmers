# 순서쌍구하기
# 두개의 수의 곱이 n이 나오도록 하는수중 몇개가 나오나
# 최대로 나올수있는수는 n의 수
# 반복문으로 길이만큼 

# 시간초과???? 너무 생각을 복잡하게했다...
def solution(n):
    answer = 0
    # 정방향 하나 역방향 하나를 구현해 코드 시간을 줄이자
    for i in range(1,n+1):
        # range(start,end,step)구조로 step에 -1를 넣으면 역순
        # reversed(range(n+1)) 같은 형식으로 reversed로도 사용 가능
        # for j in range(n,0,-1):
        #     if i*j == n:
        #         print(i,j,"i와j") 
        #         answer+=1
        #         break
        if n % i == 0:
            answer += 1
            # print(i)
        
    return answer


print(solution(20)) #6 (1, 20), (2, 10), (4, 5), (5, 4), (10, 2), (20, 1)
# print(solution(100)) #9  (1, 100), (2, 50), (4, 25), (5, 20), (10, 10), (20, 5), (25, 4), (50, 2), (100, 1)