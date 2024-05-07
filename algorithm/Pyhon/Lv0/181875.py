# 배열에서 문자열 대소문자 변환하기
# 배열에서 홀수번째 인덱스의 문자열은 모든 문자를 대문자로, 짝수번째 인덱스의 문자열은 모든 문자를 소문자로 바꿔서 반환하는 solution

def solution(strArr):
    ls=len(strArr)
    for i in range(0,ls):
        if i%2==0:
            strArr[i]=strArr[i].lower()
        else:
            strArr[i]=strArr[i].upper()
        
    return strArr

    
print(solution(["AAA","BBB","CCC","DDD"]))
