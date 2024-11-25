# 문제접근: 그래프 탐색
# YES: 1에서 시작, 다시 1로 돌아올수있음   >> 싸이클이 존재
#                       (정방향 , 역방향 방문 기록이 같아야 함)
#      + 1 이외 구역을 적어도 한번 방문할 수 있어야 함


from collections import deque

# BFS
def bfs(start, graph):
        visited = set()
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                for i in graph[node]:
                    queue.append(i) # 1:[2,3] > 2 , 3 하나 씩 추가 
        return visited


N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

# 그래프 및 역방향 그래프 
graph = {}
reverse_graph = {}
    
# 간선 입력
for s, e in edges:
    if s not in graph:
        graph[s] = [] # 정방향
    if e not in reverse_graph:
        reverse_graph[e] = []# 역방향
    graph[s].append(e)
    reverse_graph[e].append(s)
    
# 간선 정보가 없는 노드 의 경우 연걸이 없음   4: [] << 4에서 연결된 간선 없음 
for node in range(1, N + 1):
    if node not in graph:
        graph[node] = []
    if node not in reverse_graph:
        reverse_graph[node] = []
    
    
search_straight = bfs(1, graph)
search_reverse= bfs(1, reverse_graph)

# #하나 테스트 케이스를 통과 못함 (둘다 NULL일 경우 )
# if search_straight == search_reverse and len(search_straight)>1 : 
#     print(\"YES\")
# else:
#     print(\"NO\")
    
if len(search_straight &search_reverse ) > 1:  # 1번 구역 제외하고 2개 이상의 구역이 연결되어 있으면 YES
    print("YES")
else:
    print("NO")    
    