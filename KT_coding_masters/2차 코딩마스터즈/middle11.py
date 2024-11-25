# 문제접근 BFS 문제  : 워프 기술을 이용해서 (X + 3), (X - 1), (X * 2)의 위치 중 한 곳으로 이동할 수 있습니다.


from collections import deque
def BFS (start,target):
    visited = [False]*1000001
    visited[start] = True
    queue = deque([(start ,0)])
    
    while queue:
        
        now_num , steps = queue.popleft()
        
        if now_num == target:
            return steps
        
        for i in (now_num+3 , now_num-1 , now_num*2):
            if (0 <=i <=100000) and  (visited[i] == False): 
                visited[i]= True
                queue.append((i,steps+1))

now , target  = map(int , input().split())

print(BFS(now,target))
    
    
    
    


