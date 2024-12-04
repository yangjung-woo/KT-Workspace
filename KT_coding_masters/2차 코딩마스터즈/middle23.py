from collections import deque

def rabbit_maze(n, m, maze):
    # 방향 벡터 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * m for _ in range(n)]
    queue = deque([(0, 0, 0)])  # (x, y, 시간)
    visited[0][0] = True

    while queue:
        x, y, time = queue.popleft()

        # 도착점에 도달하면 시간 반환
        if x == n - 1 and y == m - 1:
            return time

        # 네 방향으로 이동
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 첫 번째 칸 이동 가능 확인
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maze[nx][ny] == '.':
                visited[nx][ny] = True  # 방문 처리

                # 두 번째 칸 이동 가능 확인
                nnx, nny = nx + dx, ny + dy
                if 0 <= nnx < n and 0 <= nny < m and not visited[nnx][nny] and maze[nnx][nny] == '.':
                    visited[nnx][nny] = True
                    queue.append((nnx, nny, time + 1))  # 두 칸 이동
                else:
                    queue.append((nx, ny, time + 1))  # 한 칸 이동

    # 도달할 수 없는 경우
    return -1

# 입력 처리
n, m = map(int, input().split())
maze = [input().strip() for _ in range(n)]

# 결과 출력
print(rabbit_maze(n, m, maze))