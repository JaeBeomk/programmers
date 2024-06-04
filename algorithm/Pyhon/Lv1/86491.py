# 최소직사각형
# 명함의 가로 세로가 주어질때 가장 최적의 직사각형 구하기
# 2중 배열인데 눕힐수 있으니... 길이가 맞으면 될것같다.

def solution(sizes):
    answer = [0,0]
    for i in sizes:
        i=sorted(i)
        # print(i)
        if i[0] > answer[0]:
            answer[0]=i[0]
        
        if i[1] > answer[1]:
            answer[1]=i[1]
    
    return answer[0]*answer[1]

def sol2(size):
    answer=[]
    a=0
    b=0
    for i ,j in size:
        if i <j:
            i,j=j,i
            
        # 더 큰수로 업데이트
        a=max(a,i)
        b=max(b,j)
    return a*b
        


# print(solution([[60, 50], [30, 70], [60, 30], [80, 40]])) # 4000
# print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])) # 120
print(sol2([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])) # 133
