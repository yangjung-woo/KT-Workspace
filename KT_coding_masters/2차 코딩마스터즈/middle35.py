# 문제접근: N 은 최대 10*5 >> , k번 리스트를 순회하게되면 시간초과(완전탐색 x )
# 다른 규칙이 있지 않을까?

# 반드시 k 일 이상 봐야 모든 배우를 볼 수 있음 
# k일씩 확인 >> 슬라이딩 윈도우 방식?
 

n , k = map(int,input().split())
actors = list(map(int, input().split()))

left = 0
actor_count = {} # actor 정보를 넣을 딕셔너리 
unique_count = 0
min_days = float('inf')
    
for right in range(n):
    # 현재 배우를 윈도우에 추가
    if actors[right] not in actor_count:
        actor_count[actors[right]] = 0
    actor_count[actors[right]] += 1
    
    if actor_count[actors[right]] == 1:  # 새로운 배우가 추가된 경우
        unique_count += 1

    # 모든 배우가 포함된 경우
    while unique_count == k:
        min_days = min(min_days, right - left + 1)
        actor_count[actors[left]] -= 1
        if actor_count[actors[left]] == 0:
            unique_count -= 1
            del actor_count[actors[left]]  # 딕셔너리에서 삭제
        left += 1
        
print(min_days)