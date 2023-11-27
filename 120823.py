# 직각삼각형 출력
# n을 입력받아 높이와 너비가 n인 직각 이등변 삼각형 그리기
# n을 입력받아 반복으로 출력하면 되는거 아닌가?
# 3
# *
# **
# *** 이런 패턴?
n = int(input())
sum =""
for i in range(n):
    sum += "*"
    print(sum)