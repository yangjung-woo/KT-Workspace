from itertools import product

def is_valid_connection(N, R, B, types, edges):
    # 각 장치와 연결된 RED 및 BLUE 타입 장치의 수를 계산
    connected_R = [0] * N
    connected_B = [0] * N
    
    for u, v in edges:
        if types[u] == "RED":
            connected_R[v] += 1
        else:
            connected_B[v] += 1
        if types[v] == "RED":
            connected_R[u] += 1
        else:
            connected_B[u] += 1
    
    # 각 장치의 제약 조건 검사
    for i in range(N):
        if R[i] != -1 and connected_R[i] != R[i]:
            return False
        if B[i] != -1 and connected_B[i] != B[i]:
            return False
    return True

def solve(N, constraints):
    R = [c[0] for c in constraints]
    B = [c[1] for c in constraints]
    
    # 모든 장치의 타입 조합 생성
    types_list = list(product(["RED", "BLUE"], repeat=N))
    min_edges = float("inf")
    valid_count = 0
    
    # 모든 장치 타입 조합에 대해 검사
    for types in types_list:
        # 가능한 모든 연결 조합 생성
        edges = []
        for u in range(N):
            for v in range(u + 1, N):
                edges.append((u, v))
        
        # 부분 집합 탐색으로 최소 전선 개수 계산
        for i in range(1 << len(edges)):
            selected_edges = []
            for j in range(len(edges)):
                if (i & (1 << j)):
                    selected_edges.append(edges[j])
            
            # 조건 검사
            if is_valid_connection(N, R, B, types, selected_edges):
                edge_count = len(selected_edges)
                if edge_count < min_edges:
                    min_edges = edge_count
                    valid_count = 1
                elif edge_count == min_edges:
                    valid_count += 1
    
    if min_edges == float("inf"):
        return -1
    return min_edges, valid_count

# 입력 및 실행
N = int(input())
constraints = [tuple(map(int, input().split())) for _ in range(N)]

result = solve(N, constraints)
if result == -1:
    print(-1)
else:
    print(result[0])
    print(result[1])