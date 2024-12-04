
def card_game_with_younghee_first(n, cards):
    total_cards = len(cards)
    chulsoo_score = 0
    younghee_score = 0
    idx = 0  # 현재 카드의 인덱스

    # 영희의 첫 선택
    younghee_score += cards[idx]
    idx += 1

    # 이후 철수와 영희가 번갈아 선택
    while idx < total_cards:
        # 철수의 차례
        max_diff = float('-inf')
        best_k = 1  # 철수가 가져갈 카드 수
        for k in range(1, 4):
            if idx + k > total_cards:
                break
            # 철수가 k장을 가져갔을 때 점수
            chulsoo_take = sum(cards[idx:idx+k])
            # 영희가 다음에 가져갈 카드
            if idx + k < total_cards:
                younghee_take = cards[idx + k]
            else:
                younghee_take = 0
            # 점수 차이 계산
            diff = (chulsoo_score + chulsoo_take) - (younghee_score + younghee_take)
            if diff > max_diff:
                max_diff = diff
                best_k = k
        
        # 철수가 best_k 장의 카드를 가져감
        chulsoo_score += sum(cards[idx:idx + best_k])
        idx += best_k

        # 영희의 차례: 다음 카드 1장 가져감
        if idx < total_cards:
            younghee_score += cards[idx]
            idx += 1

    return chulsoo_score - younghee_score

# 입력 예시
n = 6
cards = [1, 5, 5, 5, 5, 5]
result = card_game_with_younghee_first(n, cards)
print(result)  # 출력: 14