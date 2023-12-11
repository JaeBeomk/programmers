# 문자열 바꿔서 찾기
# mystring을 A를 B로 B를 A로 바꾼 문자열중 pat이 있으면 1 아니면 0
# maketrans를 이용해 A->B B->A 를 바꾼 table을 생성
# translate를 이용해 table을 덮어쓰기
# if 문으로 이제 찾아보자
# 포함인지 확인하기 위해 in 함수 사용

def solution(myString, pat):
    
    table=myString.maketrans('AB','BA')
    new_myString=myString.translate(table)
    
    return 1 if pat in new_myString else 0
    

print(solution("ABBAA","AABB"))