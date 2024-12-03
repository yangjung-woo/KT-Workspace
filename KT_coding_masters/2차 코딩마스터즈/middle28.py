def count_tile_colorings(n, m):

    # n 또는 m 중 하나가 1일 경우
    if n == 1 or m == 1:
        return 3 * (2 ** (max(n, m) - 1))

    # n, m 모두 2 이상일 경우
    return 3 * (2 ** (m - 1)) + 3 * (2 ** m)

# 사용자 입력
if __name__ == "__main__":

    n ,m= map(int,input().split())

    result = count_tile_colorings(n, m)
    print(result)