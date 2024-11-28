# 문제 접근 N 은 최대 5000 , O(N**2) 시간초과 발생 예상
# 완전탐색(브루트포스 탐색 O(N**2)) >> 카데인 알고리즘 필요(최대 구간 합 O(N))



N = int(input())

moneys = list(map(int,input().split()))

#dp = moneys.copy() # 메모리제이션용 배열 (최대 이득만 저장)
# 완전 탐색
# for i in range(N):
#     for j in range(i+1,N):
#         dp[i] = max(moneys[i], sum(moneys[i:j+1]))

# 카데인 알고리즘 
max_current = moneys[0]
max_global = moneys[0]

for i in range(1, N):
    max_current = max(moneys[i], max_current + moneys[i])  # 현재까지 최대값 갱신
    max_global = max(max_global, max_current)  # 전체 최대값 갱신
print(max_global)
    
    