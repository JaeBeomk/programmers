# 개미군단 
# 개미군단이 사냥을 나감
# 장군개미는 5의 공격력을, 병정개미는 3의 공격력을 일개미는 1의 공격력이 있음
# 사냥감의 체력 hp가 매개변수로 주어질 때, 사냥감의 체력에 딱 맞게 최소한의 병력을 구성하려면 몇 마리의 개미가 필요한지를 return

def solution(hp):
    answer = 0
    # hp가 0이 될때까지반복
    while hp !=0:
        # 가장 적은 병력 구성을 위해 개미 나눔
        if hp >= 5 :
            hp= hp-5
            answer+=1
        elif hp <5 and hp >= 3:
            hp-=3
            answer+=1
        elif hp<3:
            hp -=1
            answer+=1

    return answer


print(solution(23)) # 5
