# 문제접근 : A , B , C 용액 중 가장 큰 C를 기준으로   A C B C A C...
#          A < B < C 라고 가정할때   C > B+A 이면 용액 C는 2개 이상 남아버리고 폭발함
          
liquids = list(map(int, input().split()))

liquids.sort() # 오름차순

max_l = liquids[2] # C 

remain = liquids[0] +liquids[1] # A+B 

if max_l > remain:
    print('NO')
else:
    print('YES')