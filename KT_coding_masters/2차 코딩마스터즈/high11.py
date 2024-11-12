# 문제유형 그래프: BFS 탐색 (BFS유형을 외우고 있으면 쉽게 풀수 있는 문제)
# 1. 간선 정보를 저장할 map은 dictionary로 구현 {1: [2,3,4]}   : 1번 노드에서 2 3 4 노드로 이동 가능함 1\
# 2. 정우는 반드시 1번 노드부터 시작해서 모든 방문을 탐색  >> 1번방 ~ N번 적힌 방까지 최단거리를 저장할 dict = [0,1,1,1...] 리스트 , 경로수 way[0....] 리스트
# 3. 탐색 시 분기점    1. 아직 방문하지 않은 노드 >> queue에 방문예정 추가 , dict , way 갱신   , 
#                     2. 이미 최단경로에 있는 경우  >> (기존 경로수 way  + 현재 경로수 way )% 1,000,000,7
 
from collections import deque

def count_paths(n, k, paths):
    MOD = 1_000_000_007
    
    # 그래프 생성 (일반 dict 사용)
    graph = {}
    for u, v in paths:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    
    # 거리와 경로 수 배열 초기화
    dist = [-1] * (n + 1)
    ways = [0] * (n + 1)
    dist[1] = 0
    ways[1] = 1  # 1번 방에서 시작하므로 경로의 수를 1로 설정
    
    # BFS 초기화
    queue = deque([1])
    
    while queue:
        current = queue.popleft()
        
        for neighbor in graph[current]:
            # 아직 방문하지 않은 경우
            if dist[neighbor] == -1:
                dist[neighbor] = dist[current] + 1
                ways[neighbor] = ways[current]
                queue.append(neighbor)
            # 최단 경로에 있는 경우
            elif dist[neighbor] == dist[current] + 1:
                ways[neighbor] = (ways[neighbor] + ways[current]) % MOD

    return ways[n]

# 입력 처리
n, k = map(int, input().split())
paths = [tuple(map(int, input().split())) for _ in range(k)]

# 결과 출력
print(count_paths(n, k, paths))