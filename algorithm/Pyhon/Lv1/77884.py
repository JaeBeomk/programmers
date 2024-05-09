# 약수의 개수와 덧셈
# left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 

def solution(left, right):
    answer = 0
    for num in range(left,right+1):
        print(num)
        # 약수 구하기
        result = []
        for i in range(1, int(num**(1/2))+1):
            if num%i==0:
                result.append(i)
                if i < num//i:
                    result.append(num//i)
        # print(len(result))
        if len(result) %2==0:
            answer+=num
            # print("++++++++")
        else: 
            answer-=num
            # print("-----------")
        
    return answer


print(solution(13,17)) # 43
