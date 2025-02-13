# 문제접근
# 반복문 (더이상 지울게 없을때 까지)
# 1. 전체 nxn 맵에서 2x2 가 전부 같은 문자면 지울 수 있음 
#  1-1 2x2 가 발견되었을때 즉시 지울경우 문제가 발생 (중복 2x2가 깨짐 )
#  1-2 바로 지우지 말고 좌표를 기록만 하고 일괄적으로 지우기

# 2. 지운후 아래로 down 해주는 게 필요

from collections import deque

def erase_2x2(m,n,board):
    empty_set = set() # 좌표들을 저장
    for i in range(m-1):
        for j in range(n-1):
            # 2x2 블럭 모두 같다면 지울수 있음 
            if board[i][j] == board[i+1][j] ==board[i][j+1] == board[i+1][j+1] !='0':
                empty_set.add((i,j))
                empty_set.add((i+1,j))
                empty_set.add((i,j+1))
                empty_set.add((i+1,j+1))
    return empty_set

'''

4  4   ^
3  3   ^
2  2   ^
1  1   ^   순으로 탐색  
'''               
def gravity(m,n,board):
    # 최 하단 행부터 열 번호순으로 탐색 
    for j in range(n): # 
        queue = deque([])
        for i in range(m-1,-1,-1): # 역순으로 열 탐색
            # 빈공간을 만나면 큐에 추가   / 아니면 지나감 (빈공간위에 숫자가 있다면 아래로 재배치)
            if board[i][j]=='0':
                queue.append((i,j))
            else: # 
                if queue:# 중간에 빈 공간이 있음 (중력 적용)
                    qi , qj = queue.popleft()
                    board[qi][qj] =board[i][j]
                    board[i][j] = '0'
                    queue.append((i,j))
    return board


def solution(m,n,board):
    answer = 0
    board = list(map(lambda x: list(x), board)) # 문자열을 list로 바꿔서 nxn board가 되도록
    
    while True:
        empty_set = erase_2x2(m,n,board) # 지울수 있는 좌표들을 찾음 
        # 지우기  A => '0'
        if empty_set:
            answer += len(empty_set) # 지울수 있는 블럭 수 증가
            for (i , j) in empty_set:
                board[i][j] ='0'
            # 중력 적용 
            board = gravity(m,n,board)
            # 기존 empty_set 초기화
            empty_set.clear()
        else:  # 지울수 있는 22 블록이 없으면 
            break 

    return answer

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))

