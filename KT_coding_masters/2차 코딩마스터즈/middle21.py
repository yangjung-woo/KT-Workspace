def switch_factory(N, records, Q, queries):
    # 초기 상태
    toggle_on = False
    hold_on = False
    toggle_time = 0
    hold_time = 0

    # 행동 기록 확장
    records.append((10**6 + 1, 'X'))  # 종료 시점 추가

    # 시간별 상태 추적
    prev_time = 0
    toggle_durations = []
    hold_durations = []

    for time, action in records:
        duration = time - prev_time

        # 켜진 상태의 시간 누적
        if toggle_on:
            toggle_time += duration
        if hold_on:
            hold_time += duration

        # 현재 상태 기록
        toggle_durations.append((time, toggle_time))
        hold_durations.append((time, hold_time))

        # 상태 업데이트
        if action == 'A':
            toggle_on = not toggle_on
        elif action == 'B':
            toggle_on = not toggle_on
        elif action == 'C':
            hold_on = True
        elif action == 'D':
            hold_on = False

        prev_time = time

    # 결과 계산
    results = []
    for k in queries:
        # 이진 탐색으로 해당 시점의 누적 시간 찾기
        toggle_idx = next(i for i, (t, _) in enumerate(toggle_durations) if t > k) - 1
        hold_idx = next(i for i, (t, _) in enumerate(hold_durations) if t > k) - 1

        toggle_ans = toggle_durations[toggle_idx][1]
        hold_ans = hold_durations[hold_idx][1]
        results.append((toggle_ans, hold_ans))

    return results

# 입력 처리
N = int(input())
records = [tuple(input().split()) for _ in range(N)]
records = [(int(t), o) for t, o in records]

Q = int(input())
queries = [int(input()) for _ in range(Q)]

# 결과 계산 및 출력
results = switch_factory(N, records, Q, queries)
for toggle_time, hold_time in results:
    print(toggle_time, hold_time)