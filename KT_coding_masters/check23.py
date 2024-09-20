#- 어떤 정다각형이 작도가능할 필요충분조건은, 
# 그 변의 개수가 서로 다른 페르마 소수의 곱과 2의 거듭제곱을 곱한 형태로 나타나지는 것이다.
# 
Ferma_list = [3,5,17,257,65537]
n = int(input())
answer = 'NO'
while n %2 ==0: # 2의 거듭제곱 전부 제거
    n = n//2
    

# 서로 다른 페르마 소수의 곱
for f in Ferma_list:
    if n % f ==0:
        n = n // f
        break

if n==1 or n in Ferma_list:
    answer ='YES'
        
print(answer)