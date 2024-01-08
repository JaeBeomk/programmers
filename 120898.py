# 편지
# 한자 한자를 2cm크기로 가로로만 적을때 축하문구를 적기위해 필요한 최소 길이
# 길이 그냥 *2...
def solution(message):
    answer = (len(message)*2)
    return answer


print(solution("happy birthday!")) # 30