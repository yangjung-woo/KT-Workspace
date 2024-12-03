# 문제접근: 그래프:
# 간선을 몇 개 잘라내어 이 그래프를 트리로 만듬 < 사이클이 없도록 간선을 최소화 
# 최소 간선 트리를 만들어야함 >> 크루스칼 알고리즘 
# 간선의 양 끝 정점의 아름다운 정도를 합한 것
#

import heapq

# 크루스칼 알고리즘(Union-Find) 
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

def prune_vine(N, M, w, edges):
    # 간선 리스트 만들기 (가중치는 두 정점의 아름다운 정도 합)
    edge_list = []
    for a, b in edges:
        weight = w[a - 1] + w[b - 1]
        edge_list.append((-weight, a - 1, b - 1))  # 최대 가중치를 위해 음수 사용

    # 간선을 가중치 순으로 정렬
    heapq.heapify(edge_list)

    parent = list(range(N))
    rank = [1] * N
    max_beauty = 0
    edges_used = 0

    # 크루스칼 알고리즘으로 최대 아름다움을 갖는 트리 찾기
    while edges_used < N - 1:
        weight, a, b = heapq.heappop(edge_list)
        if find(parent, a) != find(parent, b):
            union(parent, rank, a, b)
            max_beauty -= weight  # 음수로 저장했으므로 다시 양수로
            edges_used += 1

    return max_beauty

N, M = map(int, input().split())
w = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(M)]

print(prune_vine(N, M, w, edges))
