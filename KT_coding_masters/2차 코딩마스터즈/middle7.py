# 문제접근: 리스트 순회
# 철수는  card 를 i ~ i +3 까지 카드를 가져갈 수 있음 
# 영희는 철수가 가진 마지막 카드 다음카드 단 1장을 가져가야함 
# 철수가 가져간 카드 - 영희가 가져간 카드 가 최대가 되는 것을 채택 

# 만약 현재 인덱스가   n - 3 이면 남은 카드 전부는 철수가 가져감 
def max_score_difference(n, cards):
    # 철수가 먼저 시작하는 경우
    def calculate_difference(start_first):
        current_index = 0
        chulsoo_score = 0
        younghee_score = 0

        while current_index < n:
            if current_index >= n - 3:  # 남은 카드가 3개 이하일 경우
                if start_first:
                    chulsoo_score += sum(cards[current_index:])
                else:
                    younghee_score += sum(cards[current_index:])
                break

            if start_first:  # 철수가 먼저
                max_gain = float('-inf')
                best_choice = 0
                for k in range(1, 4):
                    if current_index + k <= n - 1:
                        chulsoo_gain = sum(cards[current_index:current_index + k])
                        younghee_gain = cards[current_index + k]
                        potential_gain = chulsoo_gain - younghee_gain
                        if potential_gain > max_gain:
                            max_gain = potential_gain
                            best_choice = k
                chulsoo_score += sum(cards[current_index:current_index + best_choice])
                younghee_score += cards[current_index + best_choice]
                current_index += best_choice + 1
            else:  # 영희가 먼저
                min_loss = float('inf')
                best_choice = 0
                for k in range(1, 4):
                    if current_index + k <= n - 1:
                        younghee_gain = sum(cards[current_index:current_index + k])
                        chulsoo_gain = cards[current_index + k]
                        potential_loss = younghee_gain - chulsoo_gain
                        if potential_loss < min_loss:
                            min_loss = potential_loss
                            best_choice = k
                younghee_score += sum(cards[current_index:current_index + best_choice])
                chulsoo_score += sum(cards[current_index + best_choice:current_index + best_choice+3])
                current_index += best_choice + 1 +3

        return chulsoo_score - younghee_score

    # 두 경우의 최대값을 비교
    result_chulsoo_first = calculate_difference(start_first=True)
    result_younghee_first = calculate_difference(start_first=False)
    return max(result_chulsoo_first, result_younghee_first)


# 입력 받기
n = int(input())  # 카드 개수
cards = list(map(int, input().split()))  # 카드 값들

# 결과 계산 및 출력
result = max_score_difference(n, cards)
print(result)