#Trailing Zero - 1
# 문제설명
# 수학에서 어떤 자연수의 팩토리얼이란 그 수보다 작거나 같은 모든 자연수를 곱한 것을 의미합니다. 
# 몇 개의 팩토리얼의 값을 표기하면 다음과 같습니다. 

# 10! = 3628800
# 20! = 2432902008176640000
# 30! = 265252859812191058636308480000000

# 여기에서 맨 뒤에 연속하는 0의 갯수는 수가 커짐에 따라 늘어나는 것을 관찰할 수 있습니다. 
# 이러한 맨 뒤에 연속하는 0을 Trailing Zero라고 부릅니다. 
# 진법 표기와는 상관없이 n이 커질수록 trailing zero의 갯수는 늘어나게 됩니다. 

# 예를 들어 위의 팩토리얼의 값을 7진법에서 써보면 다음과 같게 됩니다. 
# 10! = 42562410 (7)
# 20! = 4233013654405404511500 (7)
# 30! = 202013214243236331166216633513566660000 (7)

# 정수 p와 n이 주어집니다. p-진법 체계에서 n!의 trailing zero는 몇 개인지 알아내는 프로그램을 작성해주세요. 


# 문제접근 
# n! 를 p 진법으로 표현했을 때 끝에 오는 0의 개수를 구하기
# p진법의 끝에 0이 온다는것 =  n! mod p =0   > n! %  p = 0

# (keypoint) p를 소인수분해 = a**(x) x b**(y)..
#            n!에 포함된 소인수(a,b,c..) 의 개수를 구하고 p로 몇번 나눌 수 있는지 계산 
# 


from collections import Counter

# 소인수를 구하는 함수 
def prime_factors(x): # 소인수 분해 >>  2 ,3,5,
    factors = Counter() # { 소인수: 개수 } 형태로 저장할 딕셔너리   
                        # 존재하지 않는 키를 참조하면 자동으로 {"존재하지않는 키 ": 0}  으로 저장됨
    divisor = 2
    while x >= 2:
        while x % divisor == 0:
            factors[divisor] += 1
            x //= divisor
        divisor += 1
    return factors

# 주어진 소인수가 n!에 몇 번 포함되는지 계산하는 함수
# N! 를 구하고 다시 소인수 분해하려면 너무 많은 연산이 필요함
 
# N! 에서 소인수 a 가 x 번 곱해지는데 이 x를 반환해주는 함수 
# ex) 0~100 에서 2로 나누어 떨어지는 숫자 개수  = 100//2  = 50개
#                4로 나누어 떨어지는 숫자 개수 =  100 //4 = 25
#                8로                         =  100 // 8 = 12개
#                16                          = 100 // 16 = 6 
#                32                          = 100 //32 =  3
#                64                          = 100 // 64 = 1   
#                                        0~100사이 숫자중 2의 약수는 총 (50+25+12+6+3+1) = 97개
# 100!  = 2**(97) x 3**(?)
# 참고자료(https://ind2x.github.io/posts/factorial_factorization/ )
def count_factor_in_factorial(n, factor):
    count = 0
    power = factor 
    while power <= n:
        count += n // power
        power *= factor
    return count


p, n = map(int, input().split())
# p 소인수 분해
p_factors = prime_factors(p)

# 각 소인수에 대해 n! 내에서의 개수 계산
trailing_zeros = float('inf')
for factor, power in p_factors.items():
    count_in_factorial = count_factor_in_factorial(n, factor)
    # 10!의 10 소인수 분해 >   2**(2) x 5**(2)     //  2 x 5   >> 총 2개 >> 결과 2
    trailing_zeros = min(trailing_zeros, count_in_factorial // power)  

# 결과 출력
print(trailing_zeros)