# 크기가 작은 부분 문자열
# 숫자 문자열 t,p가 주어질때 t에서p와 길이가 같은 부분문자열중
# 이 부분 문자열이 나타내는 수가 p가 나타내는 수보다 작거나 같은것 return
# p의 길이만큼 t의 문자열을 나누고 그 나눈 문자열중 p보다 작은 문자열 수를 return
# t의 길이만큼 반복하며 배열에 담고 그 배열을 하나씩 비교하자..
def solution(t, p):
    answer = 0 # 낮은 문자열 수 
    # print(len(p)) # 문자열 길이
    a=[]
    b=''
    cnt=0
    # print(len(t),len(p))
    for i in range(len(t)): # t 길이만큼 반복
        for j in range(len(p)): # p 길이만큼 반복
            if cnt-1 ==len(t)-len(p): # 길이가 채워지면 멈춤
                break
            else: 
                b+=t[j+cnt] # 이 과정에서 j=[] 인데 이걸 1씩 증감 시켜야함
                # print(b)
                if len(b)==len(p):
                    a.append(b)
                    b=''
                    cnt+=1
    
    # print(a,cnt) # 배열에 쌓이나 확인
    for i in a: # a 배열 반복해 p보다 작으면 answer 수 증가
        if i <= p:
            answer +=1
    return answer

print(solution("3141592","271")) #2
print(solution("500220839878","7")) #8
print(solution("10203","15")) # 3
