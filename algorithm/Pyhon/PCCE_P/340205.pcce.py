# https://school.programmers.co.kr/learn/courses/30/lessons/340205
# 3번/수 나누기

# number = int(input())
number = 4859

answer = 0

for i in range(1,len(str(number))):
    answer += number % 100
    number //= 100
    

print(answer)


# 입 4859 출 107
