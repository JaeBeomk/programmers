# 세균증식
# 변수 n 이 주어지고 t만큼 시간이 흐르면 증식 두배로
# 그냥 제곱 하면되는거 아닌가..?
# 아니네 계속 2배씩이네?
# 2의 t승을 n이랑 곱해주자
def solution(n, t):
    
    return n*(2**t) 

print(solution(2,10))
print(solution(7,15))