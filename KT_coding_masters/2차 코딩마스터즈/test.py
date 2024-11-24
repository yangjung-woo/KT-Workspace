import sys
 
from math import ceil
 
# 입력 받기
A, B, C = map(int, input().split())
C_target = 10  # C가 10바퀴 돌아야 함
 
# A가 몇 바퀴 돌아야 하는지 계산
A_turns = (C_target * C )/ A
 
result = ceil(A_turns)
 
print(result)