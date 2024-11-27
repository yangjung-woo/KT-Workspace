# 문제접근 : NxM 격자 로 구성된 미로를 탈출하는 최단경로?? >>  BFS 알고리즘 적용 

# 고려할점: 1. 출발지점 A 와 도착점 B 의 위치를 모르기에 출발, 도착 좌표를 알려주는 코드 필요
#          2. 꿀열매 E를 먹으면 활동량 +1 이므로   추가이동 :1~2  nx = dx[i]*2 +x 반영


from collections import deque

def find_edge(n,m,board):
    # 시작 위치(A)와 탈출구(B) 찾기
    start, end = None, None
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'A':
                start = (i, j)
            elif board[i][j] == 'B':
                end = (i, j)
    return start , end 

def BFS(start , end , board,n,m):
    
    # 격자 이동
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]

    queue = deque([(start[0], start[1],False,0)]) # 시작좌표 xy , 꿀열매 여부 , 소요일
    visited = set()
    visited.add((start[0], start[1],False))
    
    while queue:
        x,y,honey,days = queue.popleft()
        
        #목적지 도달시 종료
        if (x,y) ==end:
            return days
        
        for i in range(4):     
            # 꿀열매를 먹었는가? 
            if honey:
                step = 2
            else:
                step = 1
            
            for k in range(1,step+1): # 꿀열매를 먹은 경우 활동량 증가 , +2 이동 모든 경우 탐색
                ny= y + dy[i] * k
                nx= x + dx[i] * k
                
                if 0 <= nx < n and 0 <= ny < m  and board[nx][ny] != '#':
                    new_honey = honey or board[nx][ny] == 'G' # 꿀열매 야미~  활동+1
                    if (nx, ny, new_honey) not in visited:
                        visited.add((nx, ny, new_honey))
                        queue.append((nx, ny, new_honey, days + 1))
                else:# 격자를 벗어나는 경우면 탐색할 필요 x
                    break

    


n , m = map(int, input().split())
board =[]
for i in range(n):
    board.append(list(input().strip()))

start , end = find_edge(n,m,board)
print(BFS(start, end, board,n,m))