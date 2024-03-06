# 음양더하기
# 어떤 정수들이 있다 이 정수들의 절대값을 차례로 담을 정수 배열과 부호를 차례대로 담은 배열이 주어질때 실제 정수 들의 합을 구하여라
# signs 에 담긴 값이 False면 음수로 변경 True면 양수로 *-1 로 음수

def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        # print(i) # 0,1,2
        if signs[i]==True:
            absolutes[i] *= (+1)
        elif signs[i]==False:
            absolutes[i] *= (-1)
        # 양/음수 변경 확인
        # print(absolutes[i])
        answer+=absolutes[i]
    return answer


# print(solution([4,7,12],[True,False,True])) #9
print(solution([1,2,3],[False,False,True])) #0
