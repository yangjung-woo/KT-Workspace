
# 문제접근 N 50 , A의 길이 1000 , 
# 완전탐색시  (50)**4  > 시간초과 발생   > 다른 방안 생각 >>

# 모든 원소를 곱해서 비교하지말고  모든 곱 쌍을 해시테이블에 저장해보자 

# 곱한 결과 : [(i,j) , (k,l)] 해시맵에 저장하고 i!=j!=k!=l  이면 정답 
# 해시 테이블 (딕셔너리)


N = int(input())
nums = list(map(int, input().split()))

product_dict = {}

# 모든 (i, j) 쌍에 대해 곱 계산 및 저장  O(N**2)  
for i in range(N):
    for j in range(i + 1, N):  # i < j
        product = nums[i] * nums[j]
        if product not in product_dict:
            product_dict[product] = []
        product_dict[product].append((i, j))

# 동일한 곱을 가진 쌍들 확인  O(N**2) 이하   
for pairs in product_dict.values():
    if len(pairs) > 1:  # 같은 곱을 가진 쌍이 두 개 이상
        for (a, b) in pairs:
            for (c, d) in pairs:
                # 중복 없으면 
                if len(set([a, b, c, d])) == 4:
                    print("YES")
                    exit(0)
                    
# 최종 시간복잡도  = O(N**2) + O(N**2)  = O(N**2) , N은 최대 50

print("NO")