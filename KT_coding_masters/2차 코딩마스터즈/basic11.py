# 문제접근 : 최대공약수를 찾는 문제
# math.gcd 를 사용하면 해결 

import math
n = int(input())

nums = list(map(int, input().split()))

print(math.gcd(*nums))