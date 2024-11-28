# 문제접근: 다익스트라 문제 
# 2번 의 최단경로 탐색이 필요함 
# 1 -> K (집-> 학교 최단경로)다익스트라 
# K -> N (학교 -> 회사 최단경로) 다익스트라 
import heapq

def dijkstra(start , n , graph):
    dist= [float('inf')]*(n+1)
    dist[start]=0
    
    heap = [(0,start)]
    
    while(heap):
        current_dist ,current_node = heapq.heappop(heap)
            
        # heap에서 꺼낸 최소 거리가 최단거리가 아닐 경우 skip
        if current_dist > dist[current_node]: 
            continue
        
        for neighbor , cost in graph[current_node]:
            distance = current_dist +cost
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(heap,(distance,neighbor))
    return dist

n, m, k = map(int, input().split()) # 마을개수 , 간선개수 , 학교위치 
roads = [tuple(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n + 1)]# 인접 리스트 형식 graph

for u, v, w in roads:
    graph[u].append((v, w))
    
dist_from_1 = dijkstra(1, n, graph)# 1 -> K (집-> 학교 최단경로)다익스트라 
dist_from_K = dijkstra(k, n, graph)# K -> N (학교 -> 회사 최단경로) 다익스트라 
    

print(dist_from_1[k] +dist_from_K[n])