n = int(input())

l = list(map(int, input().split()))

l.sort(reverse=True)


result = ''.join(map(str,l))

if l.count(0) >=2 and sum(l)%3 ==0:
    pass
else:
    if result == 0:
        result = 0
    else:
        result = -1
    
print(result)