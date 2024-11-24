# 문제 접근 
# 1. x ≤ y ≤ z 
# 2. z = a or c
#    y = b or c
#    x = a or b

# 상황 1. z = a 인 경우 (a는 가장 큼 ,  x ≤ y ≤ z  )
#      z = max(a,c) =   ,   x = max(a,b) = x = a 
#      (결론)  z=a 이면 x=a 가 동시에 만족되야 하고  x == z 어야 하는데  x ==y ==z 는 발생할 수 없음 

# 상황 2. z = c 인 경우 (c는 가장 큼)
#        z = max(a,c) = c   ,  y = max(b ,c) == c    >>   z == y 를 항상 만족해야 하고 
#        x = max(a,b)  는 항상 y , z 보다 작은값이 가능함 
#  
#  [최종 결론]:  3개의 수가 최댓값 연산을 해서 나올 수 있는 수이면  y ==z 를 만족해야 함 
     


x, y, z = map(int, input().split())

if y == z:
    print('possible')
else:
    print('impossible')