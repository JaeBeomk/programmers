# 콜라츠 추측
# 주어진 수가 1이될때 까지 
# 짝수면 2로 나누고
# 홀수면 3을 곱하고 1을 더하고
# 1이될때까지 반복 500번 반복할동안 1이 안되면 -1 리턴
# 1이 되면 몇번 반복했는지 리턴
# 만약 주어진게 1이면 0리턴

def solution(num):
    answer = 0
    if num==1:
        return 0
    for i in range(1,501):
        # print(i) # 진행상황
        if num %2==0: # 짝
            num/=2
        elif num%2==1: # 홀
            num=(num*3)+1
        
        if num==1:
            print(i)
            return i
        elif i==500 and num !=1:
            print(i)
            return -1




print(solution(6)) #8
print(solution(16)) #4
print(solution(626331)) #-1