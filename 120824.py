# 짝수 홀수 구하기
# %=1 , %=0 를 이용해 홀짝을 구해 배열에 대입하자

def solution(num_list):
    jjak= 0
    hol = 0
    for i in num_list:
        if i % 2==0:
            jjak +=1
        elif i % 2 ==1:
            hol +=1
    
    return [jjak,hol]
print(solution([1, 2, 3, 4, 5]))
print(solution([1,  3,  5,7]))