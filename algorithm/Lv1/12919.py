# 서울에서 김서방 찾기
# seoul의 배열중 kim의 위치 x 를 찾아 반환하는 함수
# index로 찾아 format으로 넣어버리자
def solution(seoul):
    x=seoul.index("Kim")
    # print(x)
    
    return "김서방은 {}에 있다".format(x)

print(solution(["Jane", "Kim"])) # "김서방은 1에 있다"