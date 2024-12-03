# 문제접근: 그래프 BFS 탐색

# 두개의 컨테이너를 모두 확인해야 함 
# queue(컨테이너1, 컨테이너2,이동횟수 )

from collections import deque

def solve_containers(N, M, S1, D1, S2, D2, roads):
    # 인접 리스트 생성
    graph = [[] for _ in range(N + 1)]
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)
    
    # BFS를 위한 큐 초기화: (컨테이너1 위치, 컨테이너2 위치, 이동 횟수)
    queue = deque([(S1, S2, 0)])
    visited = set((S1, S2))
    
    while queue:
        pos1, pos2, moves = queue.popleft()
        
        # 두 컨테이너가 목표지에 도달했는지 확인
        if pos1 == D1 and pos2 == D2:
            return moves
        
        # 컨테이너 1 이동
        for next_pos1 in graph[pos1]:
            if next_pos1 != pos2 and (next_pos1, pos2) not in visited:
                visited.add((next_pos1, pos2))
                queue.append((next_pos1, pos2, moves + 1))
        
        # 컨테이너 2 이동
        for next_pos2 in graph[pos2]:
            if next_pos2 != pos1 and (pos1, next_pos2) not in visited:
                visited.add((pos1, next_pos2))
                queue.append((pos1, next_pos2, moves + 1))
    
    # 목표지에 도달할 수 없는 경우
    return -1

# 입력 처리
N, M = map(int, input().split())
S1, D1, S2, D2 = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(M)]

# 문제 해결 및 출력
result = solve_containers(N, M, S1, D1, S2, D2, roads)
print(result)
