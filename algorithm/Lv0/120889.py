# 삼각형의 완성조건
# 가장 긴 변의 길이가 다른 두변의 길이의의 합보다 작아야한다.
# 3변의 길이가 담긴 배열이 주어질때 만들수 있으면 1 없으면 2 리턴
# 정렬해서 빼내고 나머지 값을 계산하자
def solution(sides):
    ss=sorted(sides)
    big=ss.pop() # 긴변
    a=sum(ss) # 나머지 합
    return 1 if big < a else 2

print(solution([1, 2, 3])) # 3이 2+1보다 작아야함
print(solution([3, 6, 2])) # 2
print(solution([199, 72, 222])) # 1