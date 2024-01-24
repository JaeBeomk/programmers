# 핸드폰번호 가리기
# 뒷자리 4개를 제외하고 *로 변경
def solution(phone_number):
    answer = ''
    # 앞자리
    # print(phone_number[:-4])
    # 뒷자리 제외하고 * 입력
    for i in range(len(phone_number[:-4])):
        answer+="*"
    # 뒷자리
    # print(phone_number[-4:])
    answer+=phone_number[-4:]
    return answer


print(solution("01033334444")) #4444
print(solution("027778888")) #8888
