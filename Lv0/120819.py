# 아이스 아메리카노
# 한잔에 5500원
# 최대 몇잔 마실수 있나 남는돈 얼마인지...
# 잔 / 남은돈을 따로 구해서 append로 추가해야하나?
# 기억에 남는거... answer=[money // 5500, money % 5500] 이게 되네?

def solution(money):
    answer = []
    ii=money//5500
    payback=money%5500
    answer.append(ii)
    answer.append(payback)
    return answer

print(solution(5500))
print(solution(15000))