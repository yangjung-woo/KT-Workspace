# 문제접근 : 그래프 탐색 , BFS(인접 노드 탐색 , 가중치 갱신 )

from collections import deque

def Search_graph(N, M, K, weights, edges):
    total_cost = 0
    # 인접 리스트 만들기
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)

    # 가중치 차이가 초과한 경우 변경 필요 
    changed = True
    while changed:
        changed = False
        for u in range(N): # dd
            for v in adj[u]:
                if u < v:  # 간선 중복 처리 방지
                    weight_diff = abs(weights[u] - weights[v])
                    if weight_diff > K:
                        # 비용 계산
                        cost = weight_diff - K
                        total_cost += cost
                        # 가중치가 작은 쪽을 K 이하로 맞추기
                        if weights[u] < weights[v]:
                            weights[u] += cost
                        else:
                            weights[v] += cost
                        changed = True # 가중치가 갱신되었으니 전체 조정
    return total_cost

N, M, K = map(int, input().split())
weights = [int(input()) for _ in range(N)]
edges = [tuple(map(int, input().split())) for _ in range(M)]

print(Search_graph(N, M, K, weights, edges))