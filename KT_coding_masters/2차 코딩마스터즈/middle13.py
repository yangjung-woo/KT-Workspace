def dfs(x, y, direction, N, visited, path):
    if len(path) == N:
        visited.add(tuple(path))  # 경로의 고유성 확보
        return
    
    # 좌회전 (왼쪽으로 90도)
    left = (direction - 1) % 4
    dx, dy = directions[left]
    new_x, new_y = x + dx, y + dy
    if (new_x, new_y) not in path:
        dfs(new_x, new_y, left, N, visited, path + [(new_x, new_y)])
    
    # 우회전 (오른쪽으로 90도)
    right = (direction + 1) % 4
    dx, dy = directions[right]
    new_x, new_y = x + dx, y + dy
    if (new_x, new_y) not in path:
        dfs(new_x, new_y, right, N, visited, path + [(new_x, new_y)])


# 상, 우, 하, 좌 방향에 대한 좌표 변화 (시계방향)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 입력 받기
N = int(input().strip())

visited = set()
dfs(0, 0, 1, N, visited, [(0, 0)])

# 결과 출력
print(len(visited))