def can_win(word_list, current_word, turn, used):
    for i, word in enumerate(word_list):
        if not used[i] and current_word[-1] == word[0]:
            used[i] = True
            # 상대방이 이길 수 없다면 현재 플레이어 승리
            if not can_win(word_list, word, 1 - turn, used):
                used[i] = False
                return True
            used[i] = False
    # 더 이상 유효한 단어를 고를 수 없다면 상대방 승리
    return False

def shiritori_winner(n, words):
    used = [False] * n
    # 가영의 턴에서 시작하며 가영이 이길 수 있는지 확인
    if can_win(words, "", 0, used):
        return "gayeong"
    else:
        return "nayeong"

# 입력 받기
n = int(input())
words = [input().strip() for _ in range(n)]

# 결과 출력
print(shiritori_winner(n, words))