# 문제접근 : 1. 리스트에 전부 넣어서 스왑 반복하고 , 최종 단계 후 공 위치를 찾아야 함
# 리스트에 넣고 현재 공 위치가 포함되어 있으면 공 위치 갱신 

n , m = map(int, input().split())

swaps = []
for _ in range(m):
    swaps.append((map(int, input().split())))
    
ball = int(input())

for a , b in swaps:
    
    if a==ball:
        ball = b
        
    elif b ==ball:
        ball =a
        
    else: # 공 변경에 영향을 주지 않음 pass 
        pass

print(ball)