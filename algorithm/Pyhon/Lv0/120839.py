# 가위바위보
# 가위는 2 바위는 0 보는 5
# 가위 바위 보를 내는 순서대로 나타낸 문자열 rsp가 매개변수로 주어질 때, rsp에 저장된 가위 바위 보를 모두 이기는 경우를 순서대로 나타낸 문자열을 return하도록 solution 함수를 완성해보세요.
# dictionary 구조 사용

def solution(rsp):
    answer=''
    for i in rsp:
        # print(i)
        ans={"2":"0","0":"5","5":"2"}.get(i)
        answer+=ans
    return answer

#  획기적인 답이네?
def sol(rsp):
    ans={"2":"0","0":"5","5":"2"}
    return ''.join(ans[i] for i in rsp)
    

# print(solution("2")) # 0
print(sol("205")) # 052
