def calculate_fence_cost(n, trees):
    # x 좌표와 y 좌표 각각 정렬
    x_coords = sorted([x for x, y in trees])
    y_coords = sorted([y for x, y in trees])

    results = []

    # 포함할 닭나무 수: N - 4, N - 3, N - 2, N - 1, N
    for k in range(4, -1, -1):
        # 포함할 닭나무 수
        include_count = n - k

        # 최소 및 최대 x, y 좌표 선택
        x_min = x_coords[:include_count]
        x_max = x_coords[-include_count:]
        y_min = y_coords[:include_count]
        y_max = y_coords[-include_count:]

        # 울타리 비용 계산
        width = max(x_max) - min(x_min)
        height = max(y_max) - min(y_min)
        cost = 2 * (width + height)

        results.append(cost)

    return results


# 입력 처리
n = int(input())
trees = [tuple(map(int, input().split())) for _ in range(n)]

# 결과 계산 및 출력
results = calculate_fence_cost(n, trees)
for cost in results:
    print(cost)
