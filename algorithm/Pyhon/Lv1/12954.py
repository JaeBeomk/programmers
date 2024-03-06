# x만큼 간격이 있는 n의 개수
# x/n을 입력 받아 x~ 시작해 x 씩 증가하는 숫자를 n개 지나는 리스트 리턴
# sqrt = n**(1/2) 제곱근...
def solution(x, n):
    answer = []
    for i in range(n):
        print(i)
        if i==0:
            answer.append(x)
        else:
            answer.append(x*(i+1))
    return answer

print(solution(2,5))
print(solution(4,3))
print(solution(-4,2)) # -4.-8