# 부족한 금액 계산하기
# 놀이기구의 원래 이용료는 price원 인데, 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배를 받기로 하였습니다. 
# 즉, 처음 이용료가 100이었다면 2번째에는 200, 3번째에는 300으로 요금이 인상됩니다.
# 놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 

def solution(price, money, count):
    N=1
    Nprice=0
    for i in range(count):
        Nprice=price*N
        money-=Nprice
        N+=1
    money*=-1 if money < 0 else  0
    return money

print(solution(3,20,4)) # 10
