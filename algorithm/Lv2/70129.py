# 이진 변환 반복하기
# 0 과 1로 이루어진 어떤 문자열 x 에 대해 이진 변환
# 변환 과정에서 x 가 1이 될때까지 변환 횟수와 사라진 0의 수
# 0을 제거한수를 이진 변환

def solution(s):
    delzero=0 # 0 삭제 횟수
    cnt=0 # 변환 횟수 
    # s의 길이가 1이 될때까지 반복
    while len(s) !=1:
        # s가 1이 아니라면 이진 변환을 시작
        if s !="1":
            # 0이 s 에 있으면? 0을 제거하고 개수 체크 
            if "0" in s:
                delzero+=s.count("0")
                s=s.replace("0","")
                # 0을 제외한 길이를 리턴 
                s=len(s)
                # print(s)
                # 이진수로 변환 내장 함수 사용
                s=bin(s)
                s=s.replace("0b","")
                cnt+=1
                # print(s)
            elif "0" not in s:
                s=len(s)
                # 이진수로 변환 내장 함수 사용
                s=bin(s)
                s=s.replace("0b","")
                cnt+=1
                # print(s)
    if s=="1":
        return [cnt,delzero]


print(solution("110010101001")) # [3,8]
print(solution("01110")) # [3,3] 
print(solution("1111111")) # [4,1]