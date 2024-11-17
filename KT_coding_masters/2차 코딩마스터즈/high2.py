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

# 피보나치 수열은 
#  Fn  =   [[1,1]] **N   * [F(1)=1  
#          [[1,0]]          F(0)=0]

# 피보나치 수열의 점화식을 행렬 형태로 변환하여 분할 정복 방식으로 계산하면 시간 복잡도를  O(logN)으로 줄일 수 있음 
# 백준 11444 피보나치 수 6  (골드3 , 분할정복 문제 )
# 참고자료 https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-11444-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%88%98-6-%EA%B3%A8%EB%93%9C3-%EB%B6%84%ED%95%A0-%EC%A0%95%EB%B3%B5 
MOD = 1_000_000_007

def matrix_multiply(A, B):  # A x B 행렬연산
    # 결과 행렬 초기화
    result = [[0, 0], [0, 0]]
    # 행렬 A와 B의 곱셈
    for i in range(2):  
        for j in range(2):  
            for k in range(2): # A의 열과 B의행 곱
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD
    return result

def matrix_pow(base, N): # 행렬의 N 제곱을 이진 제곱법을 사용해서 O(logN)으로 수행
    result = [[1, 0], [0, 1]]  # 단위 행렬
    
    while N > 0:
        if N % 2 == 1:
            result = matrix_multiply(result, base)
        base = matrix_multiply(base, base)
        N //= 2
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

N = int(input())

print(count_mold(N))