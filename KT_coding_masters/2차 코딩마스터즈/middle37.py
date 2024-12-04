# 문제접근 : 규칙이 있는거 같아! 

# 1. 0번 컴퓨터와 연결된 1차 허브 컴퓨터 :H  m*(i-1)+1   (i =0,1,2..N)
# 2. 1차 허브 컴퓨터와 연결 가능한 컴퓨터 S = [H : H+m-1]  > >  //m 했을때 몫이 모두 같음 
# 3. 접속 기록이 맞는지 확인하는 is_connected(a,b)를 만들자 
def is_connected(a, b):
    
    # 0번 컴퓨터와 연결된 1차 허브 컴퓨터
    if a == 0 or b == 0:
        return b in hub_1st or a in hub_1st
        
    # 2. 1차 허브 컴퓨터와 연결 가능한 컴퓨터
    hub_a = (a - 1) // m
    hub_b = (b - 1) // m
    return hub_a == hub_b


n, m = map(int, input().split())
l = int(input())
log = list(map(int, input().split()))


# 1차 허브 컴퓨터 목록 생성
hub_1st = [m * i + 1 for i in range(n)]

valid = True
for i in range(l - 1):
    if not is_connected(log[i], log[i + 1]):
        valid = False
        break


print("YES" if valid else "NO")