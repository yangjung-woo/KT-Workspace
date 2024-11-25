# 문제접근  : N은 최대 10**12  < 1부터 10**12까지 모두 배열에 저장하고 계산 불가능
# 규칙이 있지 않을까?
# middle을 기준으로 k가 middle 보다 작으면 홀수 (2k-1) 
#                   k가 middle 보다 크면 짝수   (k -= middle , 2k)
 
n , k = map(int, input().split())

if n %2 ==0: # 짝수일때
    middle = n//2
else:
    middle = n//2 +1
    
if k > middle: # 짝수 area
    k -= middle
    print(2*k)
else:# 홀수 area
    print(2*k -1)
    