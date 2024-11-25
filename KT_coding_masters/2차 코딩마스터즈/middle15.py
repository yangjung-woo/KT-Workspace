# 문제접근: 슬라이딩 윈도우 + 그리디?
# 1. 싱크홀들을 오름차순 정렬
# 2. 싱크홀이 보이면 덮고 널빤지 길이만큼도 커버가 됨  >> 널판지로 커버된 현재 위치  = current_end 
# 3. 싱크홀 위치 > current_end  이면 널판지가 더 필요 



n,k = map(int, input().split())

hole = list(map(int, input().split()))

hole.sort()

current_end = -1 # 현재 널판지로 커버된 최대 위치 
planks = 0
for h in hole:
    if h > current_end:
        planks +=1
        current_end = h + k-1

print(planks)
        