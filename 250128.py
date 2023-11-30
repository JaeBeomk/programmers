# pcce 기출6번 가채점
# 한줄만 바꿔서 문제 해결하기
def solution(numbers, our_score, score_list):
    answer = []

    for i in range(len(numbers)):
        print (i," iiiiiiii")
        print(numbers[i],"nn")
        print(our_score[i],"ourrrr")
        print(score_list[i],"listttt")
        # if numbers[our_score[i]]=score_list[i]:
        # 변경
        if our_score[i] == score_list[numbers[i]-1]:
            answer.append("Same")
        else:
            answer.append("Different")
    return answer

print(solution([1],[100],[100,80,90,84,20]))

print(solution([3,4],[85,93],[85, 92, 38, 93, 48, 85, 92, 56]))