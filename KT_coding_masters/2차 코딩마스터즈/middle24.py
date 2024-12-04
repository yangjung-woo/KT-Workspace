from collections import defaultdict

def calculate_max_expectation(n, numbers):
    # 주사위 3개의 합 T의 확률을 미리 계산
    dice_prob = defaultdict(int)
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                dice_prob[i + j + k] += 1
    total_cases = 6 ** 3  # 주사위 총 경우의 수: 216
    
    # 각 T에 대한 확률 계산
    probabilities = {t: dice_prob[t] / total_cases for t in range(3, 19)}
    
    max_expectation = float('-inf')
    best_k = []
    
    # 모든 K에 대해 기댓값 계산
    for k in range(1, n + 1):
        expectation = 0
        for t in range(3, 19):
            idx = k + t
            if idx > n:
                expectation += probabilities[t] * -100
            else:
                expectation += probabilities[t] * numbers[idx - 1]
        
        # 최대 기댓값 갱신
        if expectation > max_expectation:
            max_expectation = expectation
            best_k = [k]
        elif expectation == max_expectation:
            best_k.append(k)
    
    # 결과 출력
    return int(max_expectation * 216), best_k

# 입력 처리
n = int(input())
numbers = list(map(int, input().split()))

# 결과 계산
max_expectation, best_k = calculate_max_expectation(n, numbers)

# 출력
print(max_expectation)
print(*best_k)