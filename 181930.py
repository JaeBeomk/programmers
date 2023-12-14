# 주사위게임 2
# 1 - 6 까지 주사위가 세걔
# 각 a,b,c일 때 모두 다르면 a+b+c 
# 두개만 같다면 (a+b+c)*(a^2+b^2+c^2)
# 모두 같다면(a+b+c)*(a^2+b^2+c^2)*(a^3+b^3+c^3)
# 제곱은 a**2 세제곱은 a**3으로 표현 가능하다는걸 깨달았다.


def solution(a, b, c):
    
    sum=(a+b+c)
    sum2=(a*a)+(b*b)+(c*c)
    sum3=(a*a*a)+(b*b*b)+(c*c*c)
    if a==b==c:
        return int(sum*sum2*sum3)
    elif (a!=b and b==c or a==c) or (a!=c and b==c or a==b) or (b !=c and b==a or c==a):
        
        return int(sum*sum2)
    elif a!=b and b!=c and a!=c:
        return int(sum)
        
        

print(solution(2,6,1)) # 9
print(solution(5,3,3)) # 473
print(solution(4,4,4)) # 110592