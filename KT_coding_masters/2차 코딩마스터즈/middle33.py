# 문제 접근 N 은 최대 5000 , O(N**2) 까지는 시간초과 X 
# 완전탐색(브루트포스 탐색)

N = int(input())

moneys = list(map(int,input().split()))

dp = moneys.copy() # 메모리제이션용 배열 (최대 이득만 저장)

for i in range(N):
    for j in range(i+1,N):
        dp[i] = max(moneys[i], sum(moneys[i:j+1]))
    
print(max(dp))
    
    