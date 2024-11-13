
n = int(input())

init_y , init_x = map(int,input().split())

answer = []
for _ in range(n-1):
    y , x  = map(int,input().split()) 
    
    mov_x = x - init_x
    mov_y = y - init_y
    
    # 영이의 강아지는 좌표축과 평행하게만 이동한다고 가정 
    # 
    
    if mov_x >0 and mov_y==0: # 동쪽으로 이동
        answer.append((2,mov_x))
    
    if mov_x <0 and mov_y==0: # 서쪽으로 이동
        answer.append((4, -mov_x ))
    
    if mov_y > 0 and mov_x==0: #  북쪽으로 이동
        answer.append((1,mov_y))
    
    if mov_y< 0 and mov_x==0: # 남쪽으로 이동
        answer.append((3,-mov_y))
        
    init_x = mov_x + init_x
    init_y = mov_y + init_y


for a in answer:
    print(a[0], a[1])