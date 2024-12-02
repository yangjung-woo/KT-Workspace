# 문제접근 2: 모든 경우의 수 탐색  //  O(M * K)  =O(10,000)   시간초과 문제 없을듯  
# 1. 버거 수는 1~K까지  
# 2. 패티가 N 이하라면 추가 (개당 q원) 
# 3. 최소 비용만 반환   min(total, now) 
 
def solution(n, k, burgers, q): 
     
    # 패티 개수 내림차순, 가격 오름차순으로 정렬  (그리디 접근 실패) 
    # burgers.sort(key=lambda x: (-x[0], x[1])) 
    # patties ,cost = burgers[0] 
     
    min_cost = float('inf') 
     
     
    for patties , cost in burgers: 
        for i in range(1, k + 1): # 최대 버거 구매수  
            total_patties = i * patties 
            total_cost = i * cost 
             
            if total_patties < n: 
                additional_patties = n - total_patties 
                total_cost += additional_patties * q 
             
            # 최소 비용 갱신  
            min_cost = min(min_cost, total_cost) 
             
            # 패티 수가 이미 충분하면 탈출  
            if total_patties >= n: 
                break 
     
    return min_cost 
 
 
n,k = map(int, input().split()) 
m = int(input()) 
 
burgers = [] 
for _ in range(m): 
    burgers.append(list(map(int,input().split()))) 
q = int(input()) 
 
 
print(solution(n, k, burgers, q))