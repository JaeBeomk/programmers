# 약수 1~자신 까지 1씩 증가하면서 나누어 떨어지는 경우 리스트에 추가
# 시간복잡도 O(n)
def divisor(number):
    result = []
    for i in range(1, int(number**(1/2))+1):
        if number%i==0:
            result.append(i)
    return result

# 어떤 수 N의 약수는 항상 N=A∗B로 나타낼 수 있다는 점에서 착안하여, A를 구할 경우 B까지 리스트에 추가해주는 방식으로 효율 상승
# 시간 복잡도 O(n)을 O(n^1/2)
def divisor(number): 
    result = []
    for i in range(1, int(number**(1/2))+1):
        if number%i==0:
            result.append(i)
            if i < number//i:
                result.append(number//i)
        result.sort()
    return result 

# 이건 뭐지...?
# 제곱수의 약수는 홀수개이다...
# i**0.5는 i의 제곱근을 구하는 식
def divisor(number):
    answer = 0
    for i in range(number+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
