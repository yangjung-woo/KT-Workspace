# 문제접근 : 1. 창틀을 최대한 확보 , 2. 창문을 제작

N,a,b = map(int,input().split())

tobe_frame = N*b +N  # 최소 필요한 창틀 
tobe_window = N  # 최소 필요한 창문


# 1. 창틀을 최대한 확보
cnt =  (tobe_frame-1) //(a-1)

#(조건) 
if (tobe_frame-1) %(a-1)!=0: # 나누어 떨어지지 않는 경우 
    cnt +=1 

# 2. 창문 제작 
cnt = cnt + N

print(cnt)