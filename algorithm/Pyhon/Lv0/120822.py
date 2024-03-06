# 문자열 뒤집기
# python의 문자열 뒤집기는 3가지 방법이 있다.
# 문자열 슬라이싱 이용
# 반복문 이용
# reverse 함수 이용
def reverse(my_string):
    a= list(my_string)
    a.reverse()
    a= ("".join(a))
    return a
def slice(my_string):
    return my_string[::-1]
def For(my_string):
    reverse= ""
    for i in my_string:
        reverse=i + reverse
    return reverse
print(reverse("jaron"))
print(slice("bread"))
print(For("jaron"))