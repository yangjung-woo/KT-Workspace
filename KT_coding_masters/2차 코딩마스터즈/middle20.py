from collections import defaultdict, deque

def count_original_sentences(n, sentence1, sentence2):
    words1 = sentence1.split()
    words2 = sentence2.split()

    # 단어 간의 교환 관계를 저장할 그래프
    graph = defaultdict(list)
    
    # 단어 간 연결 관계를 그래프로 생성
    for word1, word2 in zip(words1, words2):
        graph[word1].append(word2)
        graph[word2].append(word1)

    # 연결 요소 탐색 (BFS)
    visited = set()
    def bfs(start):
        queue = deque([start])
        component = set()
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                component.add(node)
                for neighbor in graph[node]:
                    queue.append(neighbor)
        return component

    # 연결 요소 찾기
    components = []
    for word in words1:
        if word not in visited:
            component = bfs(word)
            components.append(component)

    # 각 연결 요소에서 가능한 조합 계산
    result = 1
    for component in components:
        size = len(component)
        result *= size  # 연결 요소 내에서 자유로운 교환 가능

    return result

# 입력 처리
n = int(input())
sentence1 = input()
sentence2 = input()

# 결과 계산 및 출력
result = count_original_sentences(n, sentence1, sentence2)
print(result)

