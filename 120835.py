# 진료순서 정하기
# 응급도에 따른 순서 구하기?
# 배열의 크기를 순번으로 바꿔주기
# cnt를 두고 그거를 늘리면 되는거 아닌가?
# 생각해보니까 정렬이 좀더 좋은거 같다...
# 일단 배열을 순차 정렬해보자
# 정렬 후 배열을 반복해 index의 위치를 찾기
# 순차 정렬을 진행해서 그런지 낮은순으로 나옴
# reverse()를 사용해 역순으로
def solution(emergency):
    ans =[]
    for i in emergency:
        cnt=1
        for j in emergency:
            if i<j: cnt+=1
        ans.append(cnt)
    return ans
                
def sol(emergency):
    answer = []
    ans=[]
    ans=sorted(emergency)
    ans.reverse()    
    for i in emergency:
        print(i)
        print(ans.index(i))
        answer.append(ans.index(i)+1)
    return answer

print(solution([3, 76, 24])) #[3,1,2]
print(solution([1, 2, 3, 4, 5, 6, 7])) #[7, 6, 5, 4, 3, 2, 1]
