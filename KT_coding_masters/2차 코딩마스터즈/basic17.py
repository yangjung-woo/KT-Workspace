# 슬라이딩 윈도우 문제 

# 4x4 맵에서 2x2 격자를 이동시켜서   X가 3개 or X 가 4개이면 yes 출력

maps = [input().strip() for _ in range(4)]


for i in range(3):
    for j in range(3):
        # 현재 2x2 윈도우에서 'X' 개수 세기
        x_count = 0
        for di in range(2):
            for dj in range(2):
                if maps[i + di][j + dj] == 'X':
                    x_count += 1
            
        # 'X'가 4개 or 4개면 이미 완성된 2x2 영역 존재
        if x_count == 4 or x_count == 3 :
            print("yes")
            exit(0)

    
# 모든 2x2 영역을 확인해도 조건을 만족하지 못하면 'no' 반환
print("no")