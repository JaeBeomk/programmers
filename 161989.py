# 덧칠하기
# 페인트 칠해진 길이가 n미터인 벽
# 페인트 벗겨진곳 덧칠하기(일부만 칠하기)
# 1미터 길이의 구역 n개로 나누고 1 - n까지 번호를 붙히고
# 페인트 칠하는 롤러의 길이는 m미터 이고
# n의 길이의 벽을 m의 길이를 가진 롤러로 칠하는데 section의 벽을 칠해야함
# 어떻게 풀어야 할까>>>??? n이 최대 길이인데 m만큼 칠한다..인데 배열의 수가 포함이여야한다.


# 다시짜야지...
def solution(n, m, section):
    answer = 0
    a=0 # 현재 칠한곳
    for i in range(n+1):
        # print(i) # 전체 길이
        if section[0]==i:
            a=i+m-1 # 처음 칠한길이
            print(a)
            answer+=1
            if a not in section:
                section.append(a)
                section.sort()
                print(section,"없어") # a를 섹션에 추가 있다면 어쩔수없지 ㅋ
                if (section.index(a)+1)+m <n:
                    answer+=1
            print(section.index(a)+1,"a위치") # a의 위치+1
            # a값이에 한번더 칠할때 총길이 보다 작으면 칠한다.
            a=section.index(a)
            if a+m <n:
                answer+=1
                # 반복문으로 짜야할듯하다...
    return answer

# print(solution(8,4,[2,3,6]))#2 2345 5678
# print(solution(5,4,[1,3])) #1 5칸을 4칸 한번에 칠할수있는데 1,3 번을 칠하려면 1번
print(solution(4,1,[1, 2, 3, 4])) #4 1 2 3 4