arr1 = input().strip()
arr2= input().strip() 

# 문제접근 : 문자열 최대길이는 1000 , 즉 1000번 완전탐색을 해도 시간초과 X 
# 파이썬의 슬라이싱을 활용해보자 
for i in range(1,len(arr1)+1):
    push_arr =  arr2[i:]+ arr2[:i]
    if arr1 == push_arr:
        print('YES')
        exit(0)

print('NO')