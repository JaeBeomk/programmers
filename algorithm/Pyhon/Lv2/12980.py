# 점프와 순간이동
# 거리 N이 주어지고 점프는 1칸을 가면 1의 건전지가 달고
# 순간이동은 (현재까지 이동 거리) X 2의 거리를 이동 가능
# 최소의 건전지 사용한 답 구하기
def solution(n):
    ans = 1 # 시작부터 0에 곱할수는 없으니 1시작
    tel=ans*2
    count=1
    for i in range(ans,n):
        print(i)
        

    return ans

print(solution(5)) #2 => 0 점 1 순 2 순 4 점5 