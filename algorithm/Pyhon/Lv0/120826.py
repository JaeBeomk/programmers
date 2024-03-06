# 특정문자 제거하기
# 문자열을 입력받고 특정 문자를 입력받아 같으면 제거
# 배열을 반복문에 넣고 조건문을 걸어서 빼내보자
def solution(my_string, letter):
    answer = ''
    for i in my_string:
        if i!=letter:
            answer +=i
    return answer
# return my_string.replace(letter,'')
# letter 자체를 공백으로 바꿔버리는 replace 를 사용한 좋은 방법같다.

print(solution("abcdef","f"))