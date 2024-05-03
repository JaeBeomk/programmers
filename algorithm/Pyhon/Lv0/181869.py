# 공백으로 구분하기1
# 단어를 앞에서 순서대로 담아! 근데 공백이면 빼

def solution(my_string):
    ans=''
    answer=[]
    for i in my_string:
        if i !=' ':
            ans+=i
        # print(i)    
        elif i==' ':
            answer.append(ans)
            ans=''
            # print(answer)
    answer.append(ans)
    return answer
def sol(my_string):
    return my_string.split(' ')


print(sol("i love you"))
