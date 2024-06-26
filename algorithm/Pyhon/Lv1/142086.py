# 가장 가까운 글자
# 문자열s가 주어질때 처음 나온애는 -1을 나중에 나온애는 처음 나온애의 가장 가까운 숫자
# 3번 틀렸다... 다시 한번 나중에 짜봐

def solution(s):
    answer = []
    ans=[]
    for i in s:
        if i not in ans:
            ans.append(i)
            answer.append(-1)
        elif i in ans:
            ans.append(i)
            a=ans.index(i)
            b=len(ans)-1
            ans.remove(i)
            i=b-a
            answer.append(i)
    # print(ans,"asasdasdasdasd")
    return answer


# print(solution("banana"))	# [-1, -1, -1, 2, 2, 2]
# print(solution("foobar"))  # [-1, -1, 1, -1, -1, -1]
print(solution("baaab")) #  [-1, -1, 1, 1, 4]
