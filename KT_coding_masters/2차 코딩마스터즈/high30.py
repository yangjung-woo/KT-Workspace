# 문제접근: i > j 까지 이동하는 경로가 존재하는지 묻는 문제 : 플로이드 와샬?
# N은최대 100이기에 100**3 을 해도 문제없이 동작할 거 같음 

N = int(input()) 

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 플로이드-와샬 알고리즘
for k in range(N):  # 중간 정점
    for i in range(N):  # 시작 정점
        for j in range(N):  # 도착 정점
            if graph[i][k] and graph[k][j]:  # i -> k -> j 경로가 존재한다면
                graph[i][j] = 1


for row in graph:
    print(" ".join(map(str, row)))