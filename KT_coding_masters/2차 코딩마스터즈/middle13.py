from itertools import product

def normalize_path(path):
    # 경로를 모든 회전과 대칭으로 변환하여 고유 경로를 생성
    rotations = []
    for _ in range(4):  # 4번 회전
        path = [(y, -x) for x, y in path]  # 90도 시계 방향 회전
        rotations.append(path)
    flipped = [(-x, y) for x, y in path]  # 대칭
    for _ in range(4):
        flipped = [(y, -x) for x, y in flipped]
        rotations.append(flipped)
    # 가장 작은 경로를 선택
    return tuple(min(rotations))

def unique_paths(n):
    # 방향: 위, 오른쪽, 아래, 왼쪽
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def dfs(x, y, d, steps, visited, path):
        if steps == 0:
            # 정규화된 경로를 집합에 추가
            normalized = normalize_path(path)
            unique_routes.add(normalized)
            return

        for turn in [-1, 1]:  # 좌회전(-1), 우회전(+1)
            next_d = (d + turn) % 4
            dx, dy = directions[next_d]
            nx, ny = x + dx, y + dy

            if (nx, ny) not in visited:
                visited.add((nx, ny))
                dfs(nx, ny, next_d, steps - 1, visited, path + [(nx, ny)])
                visited.remove((nx, ny))

    unique_routes = set()
    # 시작점: (0, 0), 초기 방향: 위(0)
    dfs(0, 0, 0, n, {(0, 0)}, [(0, 0)])
    return len(unique_routes)


# 입력 및 테스트
n = int(input())
print(unique_paths(n))
