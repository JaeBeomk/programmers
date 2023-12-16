# 신고결과 받기(92334)
# 문제가 참 길다...
# 각 유저는 한번에 한명의 유저를 신고 가능
# 한 유저를 여러 번 신고 할수 있지만 동일 유저에 대한 신고는 1회로 처리
# k 번 이상 신고된 유저는 이용 정지 이후 신고한 모든 유저에게 메일 발송
# return 값은 id_list의 담긴 id 순서대로 받은 메일 수를 담아 리턴
# report의 누가 누굴 신고했는지 나눠야한다.
# 이거를 어떻게 처리하지?
# 반복문으로 배열을 하나씩 출력해서 문자열로 나오면 배열로 나눠보자
# k 번 이상 신고 먹으면 신고한 사람한테 메일 가기
# set은 list의 중복을 제거한 집합을 만듬

def solution(id_list, report, k):
    cnt={x:0 for x in id_list} # x 가 id_list에 있으면 초기화
    mail=[0]*len(id_list)
    for i in set(report):
        # print(i)
        cnt[i.split()[1]]+=1
    for i in set(report):
        if cnt[i.split()[1]] >=k:
            mail[id_list.index(i.split()[0])]+=1
            

    return mail

print(solution(["muzi", "frodo", "apeach", "neo"],
               ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
               2))