# 문제접근: 완전탐색 >  행렬의 최대 크기는 4x4 이므로 O(N**14) 까지는 문제 없음 

# 첫째 줄 입력
N, M, X = map(int, input().split())
# 행렬 입력
matrix = [list(map(int, input().split())) for _ in range(N)]
# 결과 출력

#O(N**6) >> 2**12 >> 4 x 10*3
for x1 in range(N):
    for x2 in range(x1,N):
        for y1 in range(M):
            for y2 in range(y1,M):
                # 부분 행렬렬 합 계산 
                s = 0
                for x in range(x1,x2+1):
                    for y in range(y1 ,y2+1):
                        s += matrix[x][y]
                        
                if s ==X:
                    print('YES')
                    exit(0)

print('NO')
exit(0)
  