# 분수의 덧셈
# gcd 함수로 최대곡약수 구하기
from math import gcd

def solution(numer1, denom1, numer2, denom2):
    num3 = denom1 * numer2 + denom2 * numer1
    denom3 = denom1 * denom2
    frac_gcd = gcd(num3, denom3)
    return [num3//frac_gcd, denom3//frac_gcd]


