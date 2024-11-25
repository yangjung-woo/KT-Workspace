# 문제접근: DP? < 하지만  N 은 최대 10**9  , 이만큼의 길이를 DP로 만들면 시간초과가 발생

# 규칙:  1번째 알람:  지정 시간에 울림 : HH:MM
#        2번째 알람:  1번째 알람 + 1분뒤 울림  == HH:MM + 1
#        5번째 알람:  1+ 2+ 3+ 4 = 10 분뒤 울림    
#       K 번째 알람은 : K-1 번째 알람 + k-1분 뒤 울림   == HH:MM +   (K-1) *(k-1 +1) //2 

# (결론) 이 문제는 등차수열의 합 문제 

time = input().strip()

hour = int(time.split(':')[0])
minute = int(time.split(':')[1])

k = int(input())
during_time = k*(k-1) //2

add_h = during_time//60
add_m = during_time %60


minute_to_hour = (minute + add_m) //60
minute = (minute + add_m) % 60
hour = (hour+ add_h+ minute_to_hour) % 24

#print(str(hour)+':'+str(minute)) 테스트 케이스 오류
# 시간과 분이 두 자리 숫자가 될 수 있도록 처리    5:8  > 05:08
print(f"{hour:02}:{minute:02}")