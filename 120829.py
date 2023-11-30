# 각도기
# 예각 직각 둔각 평각을 구해라
def solution(angle):
    if angle == 180:
        return 4
    elif 180>angle>90:
        return 3
    elif angle==90:
        return 2
    elif 90>angle>0:
        return 1
def sol(angle):
    return (angle // 90) *2 +(angle%90 >0)*1

print(solution(70))