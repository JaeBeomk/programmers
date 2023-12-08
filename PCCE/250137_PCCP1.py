# 붕대감기 PCCP 1번 기출
# t초동안 붕대감고 1초마다 x 만큼 체력회복
# t초 연속 붕대감기 성공하면 y 만큼 추가체력회복
# 최대 체력보다 커지는 것은 불가능 공격 당하면 성공 초기화
# bandage 는 시전시간,초당 회복량,추가회복량
# health 는 최대 체력
# attacks는 몬스터 공격시간과 피해량
# 입출력에 맞춰 코드를 짜보자
# 일단 반복문을 짤꺼야 그런데 몬스터의 마지막 공격을 구해서 반복하자
# pop 함수를 사용해 마지막 index를 추출 time 을 구했다
# 현재 체력 에서 연속성공과  공격맞아서 초기화
# 배열의 배열값을 꺼내야한다..
# pop 함수를 사용하니... 배열값이 사라진다...
# 배열 slice 사용 [-1]로 max값 꺼내온다.
# 체력이 0밑으로 떨어지면 그 순간 반복문을 끝낼 return 값 추가
# bandT라는 변수를 선언해 시전시간 값 설계
# 공격을 맞으면 체력을 깍고 bandT 초기화
# 공격을 받는 시간은 체력이 차면 안된다...
# HP 변수를 두어 체력이 깍인걸 확인 후 치료
# bandT가 bandage[0]값과 같아지면 초기화 후 보너스
# 최대 체력을 넘기면 다시 초기화

def solution(bandage, health, attacks):
    MaxHP = health # 최대 체력
    bandage[0] # 회복시간
    MaxTime=attacks[-1][0]
    bandT=0
    for i in range(MaxTime+1):
        print("=================\n")
        print(i,"현재 턴")
        HP=health
        print(HP,"현재 HP")        
        # 공격 데미지 정립
        for j in attacks:
            if j[0]==i:
                health-=j[1]
                print(j[1],"들어온 데미지")
                bandT=0
        print(health,"health 맞은 후 현재 체력")
        
        # 치료
        if HP==health and i!=0:
            health +=bandage[1]
            print(bandage[1],"+ Healllll")
            bandT +=1
        
        # 치료 성공 보너스
        if bandT == bandage[0]:
            bandT =0
            health +=bandage[2]
            print(bandage[2],"보너스 heallll")
        
            
        # 최대체력 유지
        if health >= MaxHP:
            print("최대 체력 이상의 체력을 가질 수 없습니다.")
            health = MaxHP
        print(bandT,"p가 연속성공 차오른다")
        print(health,"health 최종 피")
        if health <= 0:
            return -1
    return health


# result = 5
# print(solution([5,1,5],30,[[2, 10], [9, 15], [10, 5], [11, 5]]))
# result = -1
# print(solution([3, 2, 7],20,[[1, 15], [5, 16], [8, 6]]))
# result = -1
print(solution([4, 2, 7],20,[[1, 15], [5, 16], [8, 6]]))