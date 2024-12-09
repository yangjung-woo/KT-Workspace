# 문제접근 : DP
# i 번째 칸에서 최대 jump[i]만큼 점프할 수 있다 
# i +1 ~ i +jump[i] 까지의 칸 j 는    dp[i]를 추가적으로 더한다 
#  dp[j]=dp[j]+dp[i], (i+1≤j≤i+jumps[i])
MOD = 1000000007

N = int(input())
jumps = list(map(int, input().split()))

# dp[i]: i번째 칸에 도달하는 경로의 수
dp = [0] * N
dp[0] = 1  # 시작점 초기화

for i in range(N):
    max_jump = jumps[i]
    for j in range(i + 1, min(i + max_jump + 1, N)):
        dp[j] = (dp[j] + dp[i]) % MOD


print(dp[-1])