# Find : 부모 노드를 찾는 함수 (경로 압축 포함)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
    
# Union : 두 그룹을 병합하는 함수 
def union(x, y):
    rootX = find(x)
    rootY = find(y)
        
    if rootX != rootY:
        if rootX < rootY:
            parent[rootY] = rootX
            size[rootX] += size[rootY]
        else:
            parent[rootX] = rootY
            size[rootY] += size[rootX]

# 같은 그룹인지 확인하는 방법 Union -Find 방법

N,M = map(int, input().split())
edges = []
for _ in range(M):
    u , v = map(int, input().split())
    edges.append((u,v))

# 부모 노드를 저장할 리스트 초기화
parent = list(range(N + 1))
size = [1] * (N + 1)  # 각 그룹의 크기

# 친구 관계에 따라 그룹 병합
for u, v in edges:
    union(u, v)
    
# 각 그룹의 대표와 크기를 기반으로 가장 큰 그룹 ID 찾기
largest_group_size = 0
largest_group_id = N + 1  # 임의로 큰 값 설정
    
for i in range(1, N + 1):
    root = find(i)  # i번 사람의 그룹 ID (대표)
    if size[root] > largest_group_size or (size[root] == largest_group_size and root < largest_group_id):
        largest_group_size = size[root]
        largest_group_id = root
    
print(largest_group_id)