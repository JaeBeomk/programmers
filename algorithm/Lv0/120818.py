# 옷가게 활인받기
# 10만 이상 5%  / 30 이상 10 % / 50 이상 20% 할인
# 지불 금액은
def solution(price):
    
    if price >= 500000:
        price = price*0.8
    elif price >= 300000:
        price = price * 0.9
    elif price >= 100000:
        price = price * 0.95
    else: price = price
    return int(price)
print(solution(580000))
print(solution(150000))
print(solution(350000))
print(solution(50000))