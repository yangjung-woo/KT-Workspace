from itertools import combinations

def is_prime(N): # 소수 판별
    if N < 2:
        return False
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            return False
    return True

def generate_pseudo_primes(N):# N 보다 작은  유사 소수 Set을 생성 
    primes = [i for i in range(2, N) if is_prime(i)]
    pseudo_primes = set()
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            product = primes[i] * primes[j]
            if product <= N:
                pseudo_primes.add(product)
    return sorted(pseudo_primes)

def solution(N): # 4분할 하면 유사 소수 3개 이상의 합으로 표현 가능한지 판별별
    # 유사 소수 생성
    pseudo_primes = generate_pseudo_primes(N)
    
    # 4개의 서로 다른 수로 분할을 시도
    for comb in combinations(range(1,N), 4): # # 1부터 N-1까지 모든 숫자에서 조합 생성
        if sum(comb) == N:
            pseudo_prime_count = sum(1 for x in comb if x in pseudo_primes)
            if pseudo_prime_count >= 3:
                return "possible"
    return "impossible"

# 입력 처리
N = int(input())
print(solution(N))