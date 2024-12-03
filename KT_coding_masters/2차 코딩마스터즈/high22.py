# 문제접근: 모든 사람이 자신의 원래 위치가 아닌 곳에 배치해야함 >> 완전순열 문제접근
# DP로 접근 X(메모리 낭비)
# 점화식: F(n) = (n-1)x(F(n-1)+F(n-2))   % mod

MOD = 998_244_353

n = int(input())
if n == 1:
    print(0)
    exit(0)
elif n == 2:
    print(1)
    exit(0)
    
prev1, prev2 = 0, 1  # D(1) = 0, D(2) = 1
for i in range(3, n + 1):
    current = (i - 1) * (prev1 + prev2) % MOD
    prev1, prev2 = prev2, current

print(prev2)


# 메모리가 낭비되는 방식  N >=10000이면 리스트를 관리하느라 저장공간이 낭비됨 
# MOD = 998_244_353
# n = int(input())
# dp = [0]*(n+1)
# dp[1] = 0
# dp[2] = 1
# for i in range(3,n+1):
#     dp[i]  = ((i-1) * (dp[i-1] +dp[i-2]))% MOD

# print(dp[n])