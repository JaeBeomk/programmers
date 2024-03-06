# 자연수 뒤집어 배열로 만들기
# 자연수를 뒤집어서 배열로 만들기
# 문자열로 담았더니 틀렸네...
def solution(n):
    answer = []
    # 배열에 담기
    for i in str(n):
        print(i)
        # 다시 int로 형변환
        answer.append(int(i))
    answer.reverse() # 뒤집기
    return answer
print(solution(12345)) #[5,4,3,2,1]