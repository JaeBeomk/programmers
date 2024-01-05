# 코드처리하기
# code를 앞부터 읽으며 문자가 1이면 mode 변경 
# mode에 따라 code를 읽으며 문자열 ret 생성
# mode는 0 / 1 이 있으며 idx 를 0부터 code 길이 -1 까지 키워나가며
# code[idx] 값에 따라 행동
# 0일때 code[idx]가 1이면 idx가 짝수일때만 ret의 맨뒤에 code[idx] 추가
# 1일때 code[idx]가 1이면 idx가 홀수일때만 ret의 맨뒤에 code[idx] 추가
# 시작은 0
# 문자열 추가는 + / 배열에서의 추가는 append
# 길이만큼 빼고 모드를 나눠 처리..
def solution(code):
    ret = ''
    mode=0
    for i in range(0,len(code)):
        if mode==0 :
            if code[i]=="1":
                mode=1
            else:
                if i%2==0:
                    ret+=code[i]
        elif mode==1:
            if code[i]=="1":
                mode=0
            else:
                if i%2==1:
                    ret+=code[i]
    if ret=="" or ret=='':
        ret="EMPTY"
    return ret

print(solution("abc1abc1abc")) # "acbac" 0짝ac 1홀b 0짝ac
print(solution(""))