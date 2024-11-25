# 문제접근: 받는 영역의 사이즈는 상관없음 
# 직선을 그었을때 만들수 있는 최대 평면의 개수 (유튜브 참고자료 )
# https://www.youtube.com/watch?v=RWaYYi-1Q3A 

# a(n) = a(n-1) +n 

# a(n) = sigma(1~n)+1   >>  n(n+1)//2 +1 

N = int(input())
line = 0
while( 1+ line *(line+1)//2) <N:
    line +=1
print(line)


