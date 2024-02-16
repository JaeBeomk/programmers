# 다음 큰 숫자
# n이 주어졌을때 n의 다음 큰 숫자 정의
# 이진수 변환시 1의 갯수가 같다.
# 이진수 변환 함수를 이용해 풀자?

def solution(n):
    x = n+1 # 다음 큰수
    
    # 이진수 변환
    bn=bin(n)
    # bn=bn.replace("0b","")
    
    bx=bin(x)
    # bx=bx.replace("0b","")
    
    # print(bn,bx,"bbbbbbb")
    # 1의 갯수 확인
    cntn=bn.count("1")
    cntx=bx.count("1")
    # print(cntn,cntx,"cntcntcntcccc")
    
    # 1의 갯수가 다를때 1씩 더해서 다시 변환
    while cntx != cntn:
        x+=1
        bx=bin(x)
        cntx=bx.count("1")
    return x

print(solution(78)) # 83
print(solution(15)) # 23