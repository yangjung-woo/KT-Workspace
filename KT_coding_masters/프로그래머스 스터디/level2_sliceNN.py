# 문제파악 
# N x N 매트릭스를 만들어야하는데 어? N <=10^7  >> 이차원 배열 탐색시 O(N**2) = 10**14 > 무조건 시간초과 
# 절대 for i in n**2 을 탐색해선 안돼 

# 규칙이 있지 않을까?
#1.  (0,0) (0,1) (0,2)    /  for i in (n) :  0~ n-1 : i     x좌표:  i//n , y좌표:  i%n 이런 규칙 발견 
#    left // n   , left % n   >> 행렬 (y,x)좌표를 구할 수 있음 

#2. (x,y)  에서  x와 y중 하나라도 1이면  1+1
#   (x,y)  에서  x와 y중 하나라도 2이면  2+1
#   (x,y)  에서  둘다 0이면    0+1    >>  Matrix[y][x] =  max(x,y) +1

#  left ~right 까지만 순회한다면 정답을 구할 수있음  >> right - left < 10**5  / 시간복잡도 초과하지 않음 


def solution(n, left, right):
    answer =[]
    for i in range(left, right+1):
        y = i //n # 몫은 y 좌표
        x = i % n # 나머지는 x좌표 
        ans = max(x,y)+1
        answer.append(ans)
    return answer