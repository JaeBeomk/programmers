# 서로 번갈아가며 등장하는 문자열
def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer+= str1[i] +str2[i]
        
    return answer