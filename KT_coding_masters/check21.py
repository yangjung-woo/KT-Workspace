n , k  = map(int,input().split())

nums = list(map(int,input().split()))

result = [0]*n 
for i in range(n): # nums[i] 를 커트라인으로 지정시 
    for j in range(n):
        if nums[i] <= nums[j]:
            result[i] += 1

# print(result)

# 합격점수를 넘기진 못했으나 인접한 점수들을 합격처리 
for i in range(n): # nums[i] 를 커트라인으로 지정시 
    for j in range(n):
        if nums[i] >  nums[j]:
            if j ==0:
                if (nums[j+1]>=nums[i]):
                    result[i] += 1
                
            elif j < n-1:
                if (nums[j-1] >= nums[i] or nums[j+1]>=nums[i]):
                    result[i] += 1
            
            else:
                if (nums[j-1] >= nums[i]):
                    result[i] += 1
                
print(result)

max_value = -99
max_index = -1
for i in range(n):
    if result[i] <= k and result[i] >max_value:
        max_value = result[i]
        max_index = i 

if max_value != -99 and max_index > -1:
    print(nums[max_index])
else:
    print(min(nums)-1)
        
        
        

