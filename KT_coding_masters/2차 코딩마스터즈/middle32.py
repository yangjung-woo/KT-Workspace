# 문제접근: DP 최장 "증가하는 부분 수열 을 찾는 문제접근
# 1차 코딩마스터즈 (중급) 약육강식 문제와 같은 알고리즘 

n = int(input())

columns = list(map(int,input().split()))

dp =[1] * n

for i in range(n): # columns 순회
    for j in range(i):  # j 는 columns i 보다 앞에있는 기둥둥들 탐색 
        if columns[i] > columns[j]: # 앞단에서 올 수 있는는 기둥이 있다면 갱신 
            dp[i] = max(dp[i], dp[j]+1)
            
print(max(dp)-1) # 왜 틀릴까??