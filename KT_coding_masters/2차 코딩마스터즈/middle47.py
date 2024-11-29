# 문제접근 : 현재시각 HH:MM에서 k분씩 더해서   앞뒤가 똑같으면 set에 추가(중복 x) , len(set)

# 몇번 반복해야지 ?  24시간 > 1440분   , k 주기이므로  1440//k 번 반복문 수행 >> k최대 전부 수행해도 시간초과 x 


time = input()

hour, minute = map(int, time.split(":"))
k = int(input())
count = 0
seen_times = set()

for _ in range(1440):  # 최대 1440번 반복
    # HH:MM 형식의 회문 시각 확인
    time_str = f"{hour:02}:{minute:02}"
    if time_str == time_str[::-1] and time_str not in seen_times:
        count += 1
        seen_times.add(time_str)
    
    print(time_str)
    # k분 추가
    minute += k
    hour += minute // 60
    minute %= 60
    hour %= 24
    
# 디버깅용 출력 (필요 없으면 제거 가능) 
#print(seen_times)

print(count)
    