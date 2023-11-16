# 분수의 덧셈
# gcd 함수로 최대곡약수 구하기
import math

def solution(denum1, num1, denum2, num2):
    num = denum1 * num2 + denum2 * num1
    deno = num1 * num2
    gcd = math.gcd(num, deno)
    return [num//gcd, deno//gcd]


