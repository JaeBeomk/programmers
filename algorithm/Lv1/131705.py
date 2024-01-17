# 삼총사
# 학생이 담긴 배열이 주어질때
# 세 학생의 정수를 더했을때 0이되면 3총사
# 반복문 3번사용해서 0 나오는거 해볼까?  아니네 ㅋ
# 반복문은 그대로 3번 사용할껀데... 시작을 다르게 해서 짜보자
# 간단하게 줄여서 짜보자....
# def solution0(number):
#     answer = 0
#     wer=[]
#     for i in range(len(number)): # 일단 반복문으로 [0]-[:-1]번 인덱스를 가져와 얘로 만들어보자
#         for j in range(i+1,len(number)): # [1]번 인덱스를 가져오자
#             for k in range(j+1,len(number)): # [2]번 값을 가져오자
#                 if number[i]+number[j]+number[k]==0 and not i==number[j]==number[k]==0: 
                    # 3개 더했을때 0 같은 index면 안되는데 잘못짠것같다...test2번이 결과값 오류 발생
#                     # print(number[i],number[j],number[k]) # 결과물
#                     ans=[number[i],number[j],number[k]]
#                     # print(ans)# 정렬하기 위해 list에 담아 sort 튜플은 sort가 안돼
#                     ans.sort()
#                     wer.append(ans)
#                     ans=()
#     # 정렬된 배열 확인
#     # print(wer)
#     # wer 반복해서 중복 제거
#     result=[] # 중복제거한 배열담고 count
#     for i in wer:
#         if i not in result:
#             result.append(i)
#             answer+=1 
#     print(result)
#     return answer

def solution(number):
    answer = 0
    # 1번부터 반복
    for i in range(len(number)):
        # 2번은 1번 배열 +1값
        for j in range(i + 1, len(number)):
            # 3번은 2번 배열 +1값
            for k in range(j + 1, len(number)):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1

    return answer   


print(solution([-2, 3, 0, 2, -5]))#2 (-2,2,0)(3,2,-5)
print(solution([-3, -2, -1, 0, 1, 2, 3])) #5 (-3,0,3),(-2,0,2),(-1,0,1),(-2,-1,3),(-3,1,2) 
print(solution([-1, 1, -1, 1])) #0