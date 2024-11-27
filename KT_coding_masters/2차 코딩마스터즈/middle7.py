def solution(N, cards):
    # DP 테이블 초기화 
    dp = [[[0] * 2 for _ in range(N)] for _ in range(N)]
    
    # 초기 설정: 한 장만 남았을 때
    for i in range(N):
        dp[i][i][0] = cards[i]  # 철수 차례
        dp[i][i][1] = -cards[i]  # 영희 차례
    
    # 부분 문제 해결
    for length in range(2, N+1):
        for left in range(N-length+1):
            right = left + length - 1
            
            # 철수 차례일 때
            # 1장, 2장, 3장 가져갈 때 안전하게 처리
            score1_candidates = [
                cards[left] + dp[left+1][right][1],  # 1장 가져가기
            ]
            if left + 2 <= right:
                score1_candidates.append(cards[left] + sum(cards[left+1:left+3]) + dp[left+3][right][1])  # 2장 가져가기
            if left + 3 <= right:
                score1_candidates.append(cards[left] + sum(cards[left+1:left+4]) + dp[left+4][right][1])  # 3장 가져가기
            
            score2_candidates = [
                cards[right] + dp[left][right-1][1],  # 1장 가져가기
            ]
            if left <= right - 3:
                score2_candidates.append(cards[right] + sum(cards[right-2:right]) + dp[left][right-3][1])  # 2장 가져가기
            if left <= right - 4:
                score2_candidates.append(cards[right] + sum(cards[right-3:right]) + dp[left][right-4][1])  # 3장 가져가기
            
            dp[left][right][0] = max(score1_candidates + score2_candidates)
            
            # 영희 차례일 때 
            # 1장, 2장, 3장 가져갈 때 안전하게 처리
            score1_candidates = [
                -cards[left] + dp[left+1][right][0],  # 1장 가져가기
            ]
            if left + 2 <= right:
                score1_candidates.append(-cards[left] - sum(cards[left+1:left+3]) + dp[left+3][right][0])  # 2장 가져가기
            if left + 3 <= right:
                score1_candidates.append(-cards[left] - sum(cards[left+1:left+4]) + dp[left+4][right][0])  # 3장 가져가기
            
            score2_candidates = [
                -cards[right] + dp[left][right-1][0],  # 1장 가져가기
            ]
            if left <= right - 3:
                score2_candidates.append(-cards[right] - sum(cards[right-2:right]) + dp[left][right-3][0])  # 2장 가져가기
            if left <= right - 4:
                score2_candidates.append(-cards[right] - sum(cards[right-3:right]) + dp[left][right-4][0])  # 3장 가져가기
            
            dp[left][right][1] = min(score1_candidates + score2_candidates)
    
    # 전체 범위에서 철수의 최적 점수 차이 반환
    return dp[0][N-1][0]

# 입력 예시
print(solution(3, [5, 1, 6]))  # 출력: 12
print(solution(6, [5, 5, 1, 5, 5, 5]))  # 출력: 24