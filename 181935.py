# 홀짝에 따라 다른 값 반환하기
# 양의 정수 n 이 변수로 주어질 때 
# 홀수이면 n 이하의 홀수의 합을 리턴
# 짝수이면 n 이하의 짝수의 제곱의 합을 리턴
# 반복문을 돌려 n 이하의 수를 구하고
# 조건문을 이용해 i가 짝수인지 홀수인지 확인
# 더해주고 제곱을 더해줬더니 홀수값 짝수값이 섞임
# 조건 추가 n 도 짝수인지 홀수인지 추가
def solution(n):
    answer = 0
    for i in range(n+1):
        if n%2==1 and i%2==1 :
            answer+=i
            
        elif n%2==0 and i %2==0:
            answer+= (i*i)
    return answer
print(solution(10))
print(solution(7))