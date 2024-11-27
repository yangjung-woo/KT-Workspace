# 문제접근 : 완전탐색 (N==100 , N**2 까지는 시간복잡도 초과하지 않음 )
# N x N 격자 모든 좌표에서 거리를 기록 ,최단 거리만 기록 

# 만약 n =100 이고 모든 맵이 H 로만 구성되어있으면 최대 시간복잡도 = O(N**4) < 10**8 시간초과 발생
# H의 위치를 추출
# 중간값에 해당하는 위치에 마을회관 설치하면 최적일 거 같음 

n = int(input())

board = []
for i in range(n):
    board.append(list(input().strip()))
    
rows, cols = [], []

# 주택 위치 추출
for i in range(n):
    for j in range(n):
        if board[i][j] == 'H':
            rows.append(i)
            cols.append(j)
# 정렬
rows.sort()
cols.sort()

# 중간값
median_row = rows[len(rows) // 2]
median_col = cols[len(cols) // 2]

min_dist = float('inf')
best_location =(0,0)

for i in range(n):
    for j in range(n):
        total_dist = sum(abs(row - i) for row in rows) + sum(abs(col - j) for col in cols)
         # 거리 합이 최소면 업데이트 (행, 열 우선 순위)
        if (total_dist < min_dist or(total_dist == min_dist and (i < best_location[0] or(i == best_location[0] and j < best_location[1])))):
            min_dist = total_dist
            best_location = (i, j)
                
print(best_location[0]+1,best_location[1]+1)