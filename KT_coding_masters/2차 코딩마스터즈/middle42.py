# 문제접근: BFS (단 두 맵 모두 이동을 해야하는 조건)
# 1. 출발점 , 도착점 좌표를 알아야함 
# 2. BFS 는 상 하 좌 우  격자맵을 BFS로 탐색
# 조건: 맵1 이 이동할순 있지만 맵2는 이동할 수 없으면  맵 2에있는 가영이는 가만히 있는다 

# 시작점과 도착점 찾기
def find_points(maps, h, w):
    start = end = None
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'E':
                end = (i, j)
    return start, end

from collections import deque

def BFS(h1, w1, map1, h2, w2, map2):
    # 방향 정의 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    start1, end1 = find_points(map1, h1, w1)
    start2, end2 = find_points(map2, h2, w2)
    
    # BFS 탐색
    queue = deque([(start1, start2, 0)])  # (미로1 위치, 미로2 위치, 이동 횟수)
    visited = set([(start1, start2)]) # 방문기록은 두 맵의 set ((x,y) , (x,y))
    
    while queue:
        (x1, y1), (x2, y2), moves = queue.popleft()
        
        # 도착 조건
        if (x1, y1) == end1 and (x2, y2) == end2:
            return moves
        
        # 이동 시도
        for dx, dy in directions:
            nx1, ny1 = x1 + dx, y1 + dy
            nx2, ny2 = x2 + dx, y2 + dy
            
            # 미로1 이동 가능 여부
            if 0 <= nx1 < h1 and 0 <= ny1 < w1 and map1[nx1][ny1] != '#':
                new_pos1 = (nx1, ny1)
            else:
                new_pos1 = (x1, y1)  # 제자리 유지
            
            # 미로2 이동 가능 여부
            if 0 <= nx2 < h2 and 0 <= ny2 < w2 and map2[nx2][ny2] != '#':
                new_pos2 = (nx2, ny2)
            else:
                new_pos2 = (x2, y2)  # 제자리 유지
            
            # 새로운 상태
            new_state = (new_pos1, new_pos2)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((*new_state, moves + 1))
    
    # 두 미로를 동시에 해결할 수 없을 때
    return -1

h1, w1 = map(int, input().split())
map1 = [input().strip() for _ in range(h1)]

h2, w2 = map(int, input().split())
map2 = [input().strip() for _ in range(h2)]

print(BFS(h1, w1, map1, h2, w2, map2))