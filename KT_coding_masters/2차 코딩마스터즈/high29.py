# 문제접근: 규칙이 있지 않을까?
# 전체 순열 개수: N! 
# 비순환 순열의 개수는 2^(N-1)
MOD = 1000000007

N = int(input())


def mod_exp(base, exp, mod):
    # 거듭제곱을 효율적으로 계산하는 함수 (모듈러 연산 포함)
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def count_cyclic_permutations(N):
    if N < 3:
        return 0
    
    # 전체 순열의 개수는 N!
    factorial = 1
    for i in range(1, N + 1):
        factorial = (factorial * i) % MOD

    # 비순환 순열의 개수:  2^(N-1) 개 
    non_cyclic = mod_exp(2, N - 1, MOD)

    # 순환 순열의 개수 = 전체 순열 - 비순환 순열
    result = (factorial - non_cyclic + MOD) % MOD

    return result

print(count_cyclic_permutations(N))