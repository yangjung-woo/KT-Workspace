# 문제유형: DP문제인가? 

# 포자 상태에서 1분이 지나면 번식 가능한 상태가 됩니다.  >> 1분전 포자의 개수는 그대로(상태만 변함)
# + 
# 번식 가능한 곰팡이는 그 이후 매 1분마다 1개의 포자를 만들어 냅니다.
# 포자가 증식하는데 2분이 걸림 >> N분의 포자 개수는 1분전 포자 개수 + 2분전 포자 개수(증식)
# !!! 어 이거 피보나치 수열 문제네 ! 

# 확인
# 0분 : 1개 
# 1분 : 1개
# 2분 : 2개
# 3분 : 3개
# 4분 : 5개 

# 난관: N이 최대  10**12 << DP 를 한다 해도 시간초과가 날 수 밖에 없음
# 파훼법: 분할정복 > 

# 피보나치 수열의 점화식을 행렬 형태로 변환하여 분할 정복 방식으로 계산하면 시간 복잡도를  O(logN)으로 줄일 수 있음 

MOD = 1_000_000_007

def matrix_multiply(A, B): # 행렬 연산 결과를 반환 
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]
    ]

def matrix_pow(mat, exp): # 행렬을 N번 제곱해서 N+1번째 피보나치 수 계산 
    result = [[1, 0], [0, 1]]  # 단위 행렬
    base = mat
    
    while exp > 0:
        if exp % 2 == 1:
            result = matrix_multiply(result, base)
        base = matrix_multiply(base, base)
        exp //= 2
    
    return result

def count_mold(N): # 곰팡이 개체 수 반환 
    if N == 0:
        return 1
    if N == 1:
        return 1
    
    # 피보나치 수열을 구하기 위한 초기 행렬
    F = [[1, 1], [1, 0]]
    result = matrix_pow(F, N)
    
    # 피보나치 수열 f(N)을 구하기 위해 result[0][0]을 반환
    return result[0][0]

# 입력
N = int(input())

# 출력
print(count_mold(N))