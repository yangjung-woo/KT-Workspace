# 문제 접근 , 리스트의 최대 개수는 N = 100개  << O(N**2)을 해도 시간초과 발생하지 않음 
# 완전탐색 

n,k = map(int, input().split())
houses = list(map(int, input().split()))

houses.sort()  # 집 좌표 정렬
max_satisfaction = -float('inf')
best_location = None

# houses 의 모든 
for location in houses:  # 각 집 좌표를 소각장 위치로 고려
    satisfaction = 0
    for house in houses:
        d = abs(house - location)  # 소각장 과의 거리 
        
        if d <= k:  # 쓰레기 소각장과 거리가 K이하인 집은 d만큼의 만족도
            satisfaction += d
        else: # K초과인 집은 -d만큼의 만족도
            satisfaction -= d
        
    # 만족도 갱신
    if satisfaction > max_satisfaction:
        max_satisfaction = satisfaction
        best_location = location
    elif satisfaction == max_satisfaction: # 만약 그런 위치가 여러개라면, 가장 좌표가 작은 곳을 출력합니다.
        best_location = min(best_location, location)
        
print(best_location)
    
