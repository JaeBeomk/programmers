# 조건 문자열
# 문자열에 따라 두 수의 크기를 비교
# ineq / eq 가 주어지고 
# ineq 는 < > 둘 중 하나
# eq 는 = ! 둘중 하나
# 두 정수 n / m 이 주어질 때 ineq / eq의 조건에 맞으면 1 아니면 0 return
# f 스트링으로 한번 전개해보자
# f 스트링으로 한번에 나열한건 좋았는데 계산이 되나?
# 구글링을 해보니 eval 을 사용하면 f스트링 값이 계산이된다.
# 비교연산자로 true/false로 나오니 1 0 으로 변경해주자
# if 문과 int 두 방법이 있다
def solution(ineq, eq, n, m):
   print(f"{n}{ineq}{eq}{m}")
   if eq == "!":
       result = eval(f"{n}{ineq}{m}")
   elif eq == "=":
       result = eval(f"{n}{ineq}{eq}{m}")
    
   return int(result) #1 if result == True  else 0 
    

print(solution("<","=",20,50)) # return 1
print(solution("<","!",60,50)) # return 0
print(solution(">","!",41,78)) # return 0
print(solution(">","=",411,78)) # return 1
 