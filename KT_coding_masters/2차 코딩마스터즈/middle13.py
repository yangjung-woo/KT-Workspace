from itertools import product

def rotate_path(path):
    """경로를 회전한 결과 반환"""
    rotated = []
    for x, y in path:
        rotated.append((-y, x))
    return rotated

def reflect_path(path):
    """경로를 반사(대칭)한 결과 반환"""
    reflected = []
    for x, y in path:
        reflected.append((-x, y))
    return reflected

def normalize_path(path):
    """경로를 정규화 (회전, 대칭을 고려하여 가장 작은 형태로 변환)"""
    candidates = [path]
    for _ in range(3):  # 90도, 180도, 270도 회전
        path = rotate_path(path)
        candidates.append(path)
        candidates.append(reflect_path(path))
    return min(candidates)

def count_unique_paths(n):
    """N번 이동에서 고유한 산책 경로의 수 계산"""
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 동, 북, 서, 남
    unique_paths = set()

    def dfs(x, y, steps, path):
        if steps == n:
            normalized = normalize_path(path)
            unique_paths.add(tuple(normalized))
            return

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in path:  # 이미 지나간 좌표는 제외
                dfs(nx, ny, steps + 1, path + [(nx, ny)])

    dfs(0, 0, 0, [(0, 0)])
    return len(unique_paths)

# 테스트
print(count_unique_paths(4))  # 출력: 6
print(count_unique_paths(8))  # 출력: 42