# 문제접근: L,R은 최대 1,000,000 , 모든 쌍을 찾으려면 시간복잡도를 초과할 것 같음(완전탐색 x)
# 규칙?
# 1. A = B +C  , L<=A<=R , L<= (b+c)<=R 을 만족해야함
# 2  B의 범위는?   L <= B <= A-R   
#   B의 최솟값: max(L, A-R )  B의 최대값: min(R,A-L)


L, R = map(int, input().split())

total_pairs = 0

for A in range(L, R + 1):  # A는 L에서 R까지 가능
    B_min = max(L, A - R)  # B의 최소값
    B_max = min(R, A - L)  # B의 최대값
        
    # B가 유효한 경우에만 쌍을 계산
    if B_min <= B_max:
        total_pairs += (B_max - B_min + 1)
        
print(total_pairs)