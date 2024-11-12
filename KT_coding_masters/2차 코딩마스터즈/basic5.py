# 격자 판 탐색 > N,M 최대 8  완전탐색을 해도 시간초과 발생 X

def max_blessing(N, M, grid):
    max_area = 0
    
    # 모든 가능한 직사각형의 왼쪽 위와 오른쪽 아래 꼭짓점을 완전 탐색합니다.(i1,ji)   ~ (i2,j2)
    for i1 in range(N):
        for j1 in range(M):
            for i2 in range(i1, N):
                for j2 in range(j1, M):
                    # 첫 번째 문자를 가져옵니다.
                    char = grid[i1][j1]
                    is_uniform = True
                    
                    # 직사각형이 모두 같은 문자로 이루어져 있는지 확인
                    for i in range(i1, i2 + 1):
                        for j in range(j1, j2 + 1):
                            if grid[i][j] != char:
                                is_uniform = False
                                break
                        if not is_uniform:
                            break
                    
                    # 동일 문자로 이루어져 있다면 면적 계산
                    if is_uniform:
                        area = (i2 - i1 + 1) * (j2 - j1 + 1)
                        max_area = max(max_area, area)
    
    return max_area

# 입력 예시
N, M = map(int, input().split())
grid = [input().strip() for _ in range(N)]

# 최대 축복 출력
print(max_blessing(N, M, grid))  

