
board = []
for i in range(3):
    board.append(list(input().strip()))
    
if board[1][1] =='0':
    print('possible')
else:
    print('impossible')

