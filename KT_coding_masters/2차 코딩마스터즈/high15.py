# 문제접근 : BFS 문제 
# 단 조건 1. 
#조건 1. |a - c| + |b - d| = 1
#조건 2. H(a, b) ≥ H(c, d)  < 점프로 최대 1번 무시가능함 
from collections import deque

def BFS(N, grid):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 동, 남, 서, 북

    # BFS 큐 초기화: (x, y, used_jump, steps)
    queue = deque([(0, 0, 0, 1)])
    visited = [[[False, False] for _ in range(N)] for _ in range(N)]
    visited[0][0][0] = True

    while queue:
        x, y, used_jump, steps = queue.popleft()

        # (N, N)에 도달한 경우
        if x == N - 1 and y == N - 1:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N:
                if not used_jump and not visited[nx][ny][1] and grid[nx][ny] > grid[x][y]:
                    # 높이가 높은 칸으로 이동 (점프 사용)
                    visited[nx][ny][1] = True
                    queue.append((nx, ny, 1, steps + 1))
                elif grid[nx][ny] <= grid[x][y] and not visited[nx][ny][used_jump]:
                    # 높이가 낮거나 같은 칸으로 이동
                    visited[nx][ny][used_jump] = True
                    queue.append((nx, ny, used_jump, steps + 1))

    return -1  # (N, N)에 도달할 수 없는 경우


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]


print(BFS(N, grid))