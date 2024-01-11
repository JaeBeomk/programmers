# 등차수열 특정한 항만 더하기
# a,d와 길이가 n인 bool배열 included가 주어질때
# 첫 항이 a 공차가 d인 등차수열에서 included[i]가 i+1항을 의미할때 1-n항 까지
# true인 항만 더한 값을 return
# 배열s 를 만들어 a 시작값을 넣은 후 d 만큼 계속 더한값을 배열에 추가한다.
# included의 true를 찾아 index 순서에 맞는 값을 더한다.
# 해결  ㅋ

def solution(a, d, included):
    answer =0
    s=[]
    s.append(a)
    for i in range(0,len(included)):
        a +=d
        s.append(a)
        # print(s)
        if included[i]==True:
            answer+=s[i]
    return answer

print(solution(3,4, [True, False, False, True, True]))
print(solution(7,1, [False, False, False, True, False,False,False]))