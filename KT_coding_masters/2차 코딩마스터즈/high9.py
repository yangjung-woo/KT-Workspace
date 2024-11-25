MOD = 1_000_000_007

def matrix_multiply(A, B):  # A x B 행렬연산
    # 결과 행렬 초기화
    result = [[0]*len(A) for _ in range(len(A))]
    # 행렬 A와 B의 곱셈
    for i in range(len(A)):  
        for j in range(len(A)):  
            for k in range(len(A)): # A의 열과 B의행 곱
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD
    return result

def mat_pow(matrix, power):
    """행렬 거듭 제곱"""
    result = [[1,0,0,0],
              [0,1,0,0],
              [0,0,1,0],
              [0,0,0,1]] # 단위 행렬
    while power:
        if power % 2:
            result = matrix_multiply(result, matrix)
        matrix = matrix_multiply(matrix, matrix)
        power //= 2
    return result

def count_ways(N):
    if N <= 3:
        return [1, 1, 2, 4][N]

    # 변환 행렬
    transform = [
        [1, 1, 1, 1],  # dp[n] = dp[n-1] + dp[n-2] + dp[n-3] + dp[n-4]
        [1, 0, 0, 0],  # dp[n-1] -> dp[n]
        [0, 1, 0, 0],  # dp[n-2] -> dp[n-1]
        [0, 0, 1, 0],  # dp[n-3] -> dp[n-2]
    ]

    # 초기 벡터
    initial = [4, 2, 1, 1]  # dp[3], dp[2], dp[1], dp[0]

    # 행렬 거듭 제곱
    result_matrix = mat_pow(transform, N - 3)
    # 결과 계산: result_matrix[0] * initial
    result = sum(result_matrix[0][i] * initial[i] for i in range(4)) % MOD
    return result

# 입력 및 실행
N = int(input())
print(count_ways(N))