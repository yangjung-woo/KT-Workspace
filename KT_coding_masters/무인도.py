# 격자 맵 탐색하고 최대 넓이를 반환 > BFS 
from collections import deque
def BFS(y,x,maps,visited):
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    maxY = len(maps)
    maxX = len(maps[0])
    queue = deque()
    queue.append((y,x))
    visited[y][x] = True
    volumn = int(maps[y][x])
    
    while queue:
        now_y , now_x = queue.popleft()
        for i in range(4):
            ny = dy[i] +now_y
            nx = dx[i] +now_x
            if 0<=ny<maxY and 0<=nx<maxX and maps[ny][nx] != 'X' and visited[ny][nx] ==False:
                queue.append((ny,nx))
                visited[ny][nx] = True
                volumn += int(maps[ny][nx])
    return volumn
def solution(maps):
    answer = []
    
    visited = [[False] * len(maps[0])  for _ in range(len(maps))]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if visited[i][j] == False and maps[i][j] != 'X':
                answer.append(BFS(i,j,maps,visited)) 
    
    if answer:
        return sorted(answer)
    else:
        return[-1]

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))