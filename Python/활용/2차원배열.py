# 2중 for문으로 2중 리스트 선언
array = [[0 for col in range(11)] for row in range(10)]
# 11x10 리스트를 생성합니다.  = (11열 10행) 

# *연산자와 for문으로 리스트 선언
array = [[0]*11 for i in range(10)]

array[3][1] = "@" 
# 4번째 행 , 두번째 열을 "@"로 바꾸는 코드. (index는 0부터 시작이므로 +1을 했다고 생각해야합니다.)

# 2중 리스트 출력
# 보기 좋게 출력하려면 for문을 이용해아 합니다. 2중 배열이기 때문에 2중 for문을 사용하여 출력합니다.
for i in array :
    for j in i:
        print(j,end=" ")
    print()
