# 나선형으로 배치하기
# n 이 주어지면 n x n 배열을 만듬 근데
# 나선형으로 배치하는??? 어떻게 하는겨...
# 이번적인 배열은 완성... 그런데 나선형?
# 아니면 2차원 배열에 하나씩 넣어보자
# 일단 배열을 초기화 해주고 
# 순서에 때려박어

def solution(n):
    if n ==1 :
        return [[1]]
    # 배열 초기화
    answer=[[0 for j in range(n)]for i in range(n)]
    x=0 # x/y 값을 초기화 해서 하나씩 집어넣자
    y=0
    
    case = 6 # 키패드 방향키 순 4862
    for i in range(n*n):
        answer[x][y]= i+1
        
        # 일단 옆으로 한줄
        if case == 6:
            y +=1
            if y == n-1 or answer[x][y+1] !=0:
                case=2
        # 밑으로 내리기
        elif case == 2:
            x +=1
            if x ==n-1 or answer[x+1][y] !=0:
                case =4
        # 옆으로 반대
        elif case ==4:
            y -= 1
            if y==0 or answer[x][y-1] !=0:
                case = 8
        # 위로 올리기
        elif case == 8:
            x -= 1
            if x ==n-1 or answer[x-1][y] !=0:
                case=6   
    return answer

# 일반적인 배열...
def sol(n):
    answer = []
    list=[]
    for i in range(1,n*n+1):
        # print(i)
        list.append(i)
        print(list)
        if i % n ==0:
            answer.append(list)
            list=[]
            
    return answer

print(solution(4))