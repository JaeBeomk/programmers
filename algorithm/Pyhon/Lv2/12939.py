# 최댓값과 최솟값
# s 에는 공백으로 구분된 숫자들
# 최솟값과 최댓값 찾아 "(최소) (최대)" 형태의 문자열 반환
# "" 가 표현되게? = > '""' 작은 따옴표로 가두기 아니네?ㅋㅋ
# 리스트의 각 요소를 정수로 변환해보자

def solution(s):
    s=s.split()
    s=list(map(int,s)) # 각 요소 형변환  
    s=sorted(s)
    # print(s)

    Mins=s[0]
    Maxs=s[-1]
    # print(Maxs,Mins)
    ans="{} {}".format(Mins,Maxs)
    return ans


# print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4 5 2"))
# print(solution("-1 -1"))