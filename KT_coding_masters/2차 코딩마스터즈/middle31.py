# 문제접근: N,K은 최대 8 , 가능한 모든 조합 전부 확인해도 되지 않을까?
# 집 방문 순서 : 8! ,    O(N!) = 최대 40320 < 문제 없을거같음 
#

from itertools import combinations, permutations # 조합 , 순열 전부 탐색 

def distance(p1, p2): # 맨해튼 거리 계산
   
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
n, k = map(int, input().split())
houses = [tuple(map(int, input().split())) for _ in range(n)]


restaurant = (1, 1)  # 식당 좌표
min_time = float('inf')
    
# 모든 조합에서 배달할 K개의 집 선택 >  # 모든 방문 순서를 탐색
for selected_houses in combinations(houses, k):
    for order in permutations(selected_houses):
        # A에서 출발 -> 집들 방문 -> A로 돌아오는 거리 계산
        time = 0
        current_position = restaurant
            
        for house in order:
            time += distance(current_position, house)
            current_position = house
            
        # 마지막 집에서 다시 A로 돌아오기
        time += distance(current_position, restaurant)
            
        # 최소 시간 갱신
        min_time = min(min_time, time)
        

print(min_time)