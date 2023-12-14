# 옹알이(1)
# 머쓱이 태어난지 6개월된 조카 돌보는중
# 애기는 힙해서 "aya" "ye" "woo" "ma" 4가지 발음가능
# babbling이 변수로 주어질때 발을할수있는 단어개수 return
# 배열을 반복해 in 함수로 찾아볼까했는데 계속 예상 결과와 다르게 나와 뭐지.. 했는데...a
# 문제를 잘못읽었네.... 요지는  한 단어를 다 읽나 못읽나이네...
# 그렇다면 어떻게 짜야지? 뭘 어케짜 천천히 짱구를 굴려보자
# 일단 일치시 정답은 완성
# 단어를 합쳐서 만들어봐야지...
# word를 공란에두고 한글자씩 받아와서 배열안의 글자와 맞으면 초기화 시키자
# 어차피 단어 전체에 발음이 가능해야하니...
# 어렵게 생각하지말고 시작부터 다르면 초기화시켜버리자
def solution(babbling):
    answer = 0
    baby= ["aya","ye","woo","ma"]
    for i in babbling:
        print("\n")
        print(i,"단어 시작")
        word=''
        cnt = 0
        for j in i:
            word +=j
            print(word,"위아더월드")
            if word in baby:
                word=''
                cnt +=1
            print(cnt,"count")
        if len(word)==0 and cnt>0:
            answer +=1
        print(len(word),'남은길이')
    return answer

print(solution(["aya", "yee", "u", "maa", "wyeoo"])) # 1
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"])) # 3

