# 삼총사
# 학생이 담긴 배열이 주어질때
# 세 학생의 정수를 더했을때 0이되면 3총사
# 반복문 3번사용해서 0 나오는거 해볼까?  아니네 ㅋ
# 반복문은 그대로 3번 사용할껀데... 시작을 다르게 해서 짜보자

def solution(number):
    answer = 0
    ans=[]
    for i in number: # 일단 반복문으로 [0]번 인덱스를 가져와 얘로 만들어보자
        for j in range(1,len(number)): # [1]번 인덱스를 가져오자
            for k in range(2,len(number)): # [2]번 값을 가져오자
                if i+number[j]+number[k]==0 and not i==number[j]==number[k]==0:
                    # print(i,number[j],number[k]) # 결과물
                    ans.insert(i,number[j],number[k])
                    print(ans)
                    # 집가서 다시
                    answer+=1

    return answer


print(solution([-2, 3, 0, 2, -5]))#2 (-2,2,0)(3,2,-5)
# print(solution([-3, -2, -1, 0, 1, 2, 3])) #5 (-3,0,3),(-2,0,2),(-1,0,1),(-2,-1,3),(-3,1,2) 
# print(solution([-1, 1, -1, 1])) #0