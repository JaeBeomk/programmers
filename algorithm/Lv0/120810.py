# 나머지
# divmod(변수,변수)[0][1] 0=몫 1=나머지
def solution(num1, num2):
    return divmod(num1,num2)[1]

print(solution(7,4))