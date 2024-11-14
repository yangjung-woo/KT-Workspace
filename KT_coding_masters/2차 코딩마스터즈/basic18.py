# 문제접근 : n 에서 지팡이를 사용할 수 있으면 사용해서 1이 되는 '최소값'(=최단경로)를 찾는 문제접근
# BFS 로 풀 수 있다! 
# 1차 코딩마스터즈에 유사한 문제가 있엇는데  숫자 맞추기(중급 문제)

from collections import deque

def can_magic(current, divisor, multiplier):
    if current % divisor == 0:
        next_val = (current // divisor) * multiplier
        return next_val
    return None


def BFS(N):
    
    if N == 1:
        return 0
    
    queue = deque([(N, 0)])  # (현재 숫자, 지팡이 사용 횟수)
    visited = set([N])       # 방문한 숫자 기록
    
    while queue:
        current, uses = queue.popleft()
        
        # 각 마법 지팡이 연산을 시도
        for divisor, multiplier in [(2, 1), (3, 2), (5, 4)]:
            next_val = can_magic(current, divisor, multiplier)
            if next_val is not None:
                if next_val == 1:
                    return uses + 1
                if next_val not in visited:
                    queue.append((next_val, uses + 1))
                    visited.add(next_val)
    
    return -1  # 1에 도달할 수 없는 경우 -1 반환

# 입력 예시
N = int(input().strip())
print(BFS(N))