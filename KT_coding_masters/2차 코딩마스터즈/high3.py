def card_shuffle(N, K, A):
    
    cards = list(range(1, N + 1))
    def apply_permutation(cards, A):
        return [cards[A[i] - 1] for i in range(N)]

    visited = [False] * N
    cycles = []

    for i in range(N):
        if not visited[i]:
            cycle = []
            current = i
            while not visited[current]:
                visited[current] = True
                cycle.append(current)
                current = A[current] - 1
            cycles.append(cycle)

    # K번 섞은 결과 계산
    result = [0] * N
    for cycle in cycles:
        cycle_length = len(cycle)
        shift = K % cycle_length
        for i in range(cycle_length):
            result[cycle[(i + shift) % cycle_length]] = cards[cycle[i]]

    return result


N, K = map(int, input().split())
A = list(map(int, input().split()))
result = card_shuffle(N, K, A)
print(" ".join(map(str, result)))
