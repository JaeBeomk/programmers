# 정수 내림차순 배치
# 정수를 하나씩 배열에 담아서 sorted로 뒤집기

def solution(n):
    answer = ''
    # 리스트로 변환 반복문 혹은 list(str(n)) 으로 간단하게 처리
    # n_list=[]
    # for i in str(n):
    #     # print(i)
    #     n_list.append(i)
    n_list=list(str(n))
    for i in sorted(n_list,reverse=True):
        answer+=i
    # string 문자열을 정수로 변환
    # print(type(answer))
    return int(answer)

print(solution(118372))