# 숫자의 표현
# 자연수 n을 연속한 자연수들로 표현하는 방법이 여러개
# 연속한 수들로 더해야한다..

def solution(n):
    answer = 0
    cnt=0
    # 반복문을 돌려 순서대로 돌린다.
    # 시작은 1부터
    for i in range(1,n+1):
        answer=0
        answer+=i
        # 뒤에수를 더한다 n이 되면 멈추고 합이 n보다 크면 멈춘다
        for j in range(i+1,n+1):
            answer+=j
            # print(i,j,"uuuiuiuiu")
            if answer==n:
                cnt+=1
                # print(answer,"asdasdas")
                # answer=0
                break
            elif answer>n:
                break
        if i==n:
            cnt+=1
    return cnt

print(solution(15)) # 4 => 1+2+3+4+5 / 4+5+6 / 7+8 / 15