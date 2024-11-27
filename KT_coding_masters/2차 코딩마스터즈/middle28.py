# 문제접근: 모든 색칠한 경우의 수를 확인 > 완전탐색?  n , m 최대 5 
def is_valid(x, y, color, board):# x,y의 색 유효성 검사  인접한 칸중 같은 색이 있으면 False ,
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == color:
            return False
    return True

def count_ways(x, y, board, n, m): # 백트래킹 , 모든 색칠 방법 탐색 
    # 1 --------->
    # 2 --------->
    # 3 ---------> 순으로 탐색 
    
    if x == n:
        return 1
    if y == m:
        return count_ways(x + 1, 0, board, n, m)
    
    ways = 0
    for color in range(1, 4):  # 1, 2, 3 색  3가지 
        if is_valid(x, y, color, board):
            board[x][y] = color
            ways += count_ways(x, y + 1, board, n, m)
            board[x][y] = 0  # 되돌리기
    return ways

def board_coloring(n, m):
    board = [[0] * m for _ in range(n)]  # 격자판 초기화 (0은 칠하지 않음)
    return count_ways(0, 0, board, n, m)


n,m =map(int,input().split())
print(board_coloring(n,m))

