# 문제접근: 다익스트라 문제 

import heapq

def dijkstra(start , n , board):
    dist= [float('inf')]*(n+1)
    dist[start]=0
    
    heap = [(0,start)]
    
    while(heap):
        current_dist ,current_node = heapq.heappop(heap)
            
            # 최단거리가 아닐 경우 skip
        if current_dist > dist[current_node]: 
            continue
            
        for neighbor , cost in graph[current_node]:
            distance = current_dist +cost
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(heap,(distance,neighbor))
    return dist

n, m, k = map(int, input().split())

graph =  [[] for _ in range(n+1)] # 인접 리스트 형식 graph
for i in range(m):
    u,v,cost = map(int, input().split())
    graph[u].append((v,cost))
    
dist_1_to_N = dijkstra(1, n, graph)
dist_K_to_N = dijkstra(k, n, graph)
    
print(dist_1_to_N[k] +dist_1_to_N[n])