# 문제접근 : X를 만났을때 스택을 확인 
# 1. 최소 섬의 개수일때:x >  g 다음  g   , o 다음 o 
# 2. 최대 섬의 개수일때:x >  g 다음 o   , o 다음 g 로 변환 
 
maps = input().strip()

max_g =0
min_g =0
min_stack= []
max_stack =[]
# 최소 섬의 개수 
for m in maps:
    if len(min_stack) ==0:
        min_stack.append(m)
    else:
        if m =='o':
            if min_stack[-1] == 'g':
                min_g +=1
            min_stack.append(m)
        elif m =='g':
            min_stack.append(m)
        
        else: # x 
            if min_stack[-1] == 'o':
                min_stack.append('o') 
            else: # stack[-1] =='g'
                min_stack.append('g')# m 대신 'g' 추가

print(min_g)
# 최고 섬의 개수 
for m in maps:
    if len(max_stack) ==0:
        max_stack.append(m)
    else:
        if m =='o':
            if max_stack[-1] == 'g':
                max_g +=1
            max_stack.append(m)
        elif m =='g':
            max_stack.append(m)
        
        else: # x 
            if max_stack[-1] == 'o':
                max_stack.append('g')  # m 대신 'g' 추가
            else: # stack[-1] =='g'
                max_stack.append('o')
                max_g +=1
print(max_g)
    
    