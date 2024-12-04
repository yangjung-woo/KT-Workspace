def sieve_of_eratosthenes(limit):
    # 에라토스테네스의 체로 소수 집합 생성
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(limit + 1) if is_prime[i]]

def min_n(k, remaining_digits):
    # \( N \)의 최소값을 찾기 위해 점진적으로 범위를 확장
    limit = 10
    while True:
        primes = sieve_of_eratosthenes(limit)
        valid_primes = []
        
        # 각 소수가 조건을 만족하는지 확인
        for prime in primes:
            prime_str = str(prime)
            is_valid = True
            for digit in remaining_digits:
                if digit not in map(int, prime_str):
                    is_valid = False
                    break
            if is_valid:
                valid_primes.append(prime)

        # 유효한 소수 중 가장 큰 값이 최소 \( N \)
        if len(valid_primes) > 0:
            return max(valid_primes)
        
        # 범위 확장
        limit *= 2

# 입력 처리
k = int(input())
remaining_digits = list(map(int, input().split()))

# 결과 출력
result = min_n(k, remaining_digits)
print(result)