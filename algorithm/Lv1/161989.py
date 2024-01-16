# 덧칠하기
# 페인트 칠해진 길이가 n미터인 벽
# 페인트 벗겨진곳 덧칠하기(일부만 칠하기)
# 1미터 길이의 구역 n개로 나누고 1 - n까지 번호를 붙히고
# 페인트 칠하는 롤러의 길이는 m미터 이고
# n의 길이의 벽을 m의 길이를 가진 롤러로 칠하는데 section의 벽을 칠해야함
# 어떻게 풀어야 할까>>>??? n이 최대 길이인데 m만큼 칠한다..인데 배열의 수가 포함이여야한다.
# 덧칠하는 시작점을 잡고 반복해서 풀면 코드도 간단해지고 정확하다.

def solution(n, m, section):
    answer = 1 # 칠하는 횟수
    paint = section[0] # 덧칠 시작점
    for i in range(1, len(section)): # 섹션 길이만큼 반복
        if section[i] >= m+ paint: # 시작점에 롤러만큼 더했을때 보다 크면 +1
            answer += 1
            paint = section[i]

    return answer

print(solution(8,4,[2,3,6]))#2 2345 5678
print(solution(5,4,[1,3])) #1 5칸을 4칸 한번에 칠할수있는데 1,3 번을 칠하려면 1번
print(solution(4,1,[1, 2, 3, 4])) #4 1 2 3 4