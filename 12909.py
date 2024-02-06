# 올바른 괄호
# 괄호가 바르게 짝지어졌다는것은 () 로 이루어져야 한다.
# 올바르면 true 다르면 false
# ( 가 나온만큼 )가 안나오면 False
# 테스트 케이스는 통과인데 뭐가 안되지...?

def solution(s):
    le=0 # 왼
    ri=0 # 오
    # 일단 맨 앞뒤가 틀리면 떙
    if s[0] !="(":
        return False
    elif s[-1] != ")":
        return False
    
    # 순서대로 나온만큼 
    for i in s:
        if i=="(": 
            le+=1
        elif i==")":
            ri+=1
            # le가 1번 나오고 ri==le 가 같고 ri+le의 갯수가 s의 길이와 같다면?
            if le>=1 and ri==le and ri+le==len(s):
                return True
            elif ri == le and ri+le < len(s):
                continue
            elif ri+le ==len(s) and ri != le:
                return False

#  그냥 하나씩 더하고 빼면 해결인가보다...
def solution(s):
    count = 0
    
    for c in s:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
            
        if count < 0:
            break
            
    return count == 0

print(solution("()()")) # True
print(solution("()())")) # False
# print(solution("(())()"))
# print(solution(")()(")) # False
# print(solution("(()("))