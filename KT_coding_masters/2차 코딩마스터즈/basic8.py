# 
import math
x,y,z = map(int, input().split())

# 문제접근: 톱니바퀴 비례식
# A_회전 * A_톱니수 = B_회전 * B_톱니수
# B_회전 * B_톱니수 = C_회전 * C_톱니수
# C_회전 = 10 
# C_톱니수 = z  ,B_톱니수 = y  , A_톱니수 = x 

# 출력값 : A_회전수 =? 
# A_회전수 = ( C_회전 * C_톱니수 ) / A_톱니수 


result = (10* z) / x # 3.1  > 적어도 4번은 회전해야 함 > 올림 math.ceil()

print(math.ceil(result))