# 최대공약수와 최소공배수
# 두 수의 최대공약수와 최소공배수를 반환
# 최대 공약수 공통된 약수중 제일 큰값


def solution(n, m):
    answer = []
    # 최대 공약수는 지수를 활용
    value=min(n,m)
    for i in range(1,value+1):
        if n%i==0 and m%i==0:
            answer.append(i)
    minv=answer[-1]
    n/=minv
    m/=minv
    # 최소 공배수는 나머지와 최대공약수의 곱
    maxv=int(minv*n*m)
    return [minv,maxv]


def solution(n, m):
    answer = []
    # 최대 공약수는 지수를 활용
    value = min(n, m)
    for i in range(value, 0, -1) :
        if n % i == 0 and m % i == 0 :
            answer.append(i)
            break
        
    # 최소 공배수는 나머지와 최대공약수의 곱
    value = max(n, m)
    for i in range(value, value * value) :
        if i % n == 0 and i % m == 0 :
            answer.append(i)
            break
            
    return answer

# print(solution(3,12)) #[3,12]
# print(solution(2,5)) #[1,10]
print(solution(36,48)) # [12,12]
