# 문제접근 : 슬라이딩 윈도우?  , 

n,k = map(int , input().split())

nums =list(map(int , input().split()))

max_visit = -99

for i in range(n-k+1):
    if max_visit < sum(nums[i:i+k]): # 최대값이 갱신되면 그 위치 i를 저장
        max_visit = sum(nums[i:i+k])
        
        idx = i+1
        
print(idx)
    
    